import streamlit as st
import mysql.connector
from mysql.connector import Error
import pandas as pd

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ksu_database"
    )

def fetch_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ksu_std_table")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    cursor.close()
    conn.close()
    return pd.DataFrame(rows, columns=columns)

def student_exists(std_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM ksu_std_table WHERE ksu_std_id = %s", (std_id,))
    (count,) = cursor.fetchone()
    cursor.close()
    conn.close()
    return count > 0

def get_student_by_id(std_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ksu_std_table WHERE ksu_std_id = %s", (std_id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row

def insert_student(std_id, name, age, dept, signin, grade):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO ksu_std_table (ksu_std_id, ksu_std_name, ksu_std_age, ksu_std_department, ksu_std_signin, ksu_std_grade) VALUES (%s, %s, %s, %s, %s, %s)",
                       (std_id, name, age, dept, signin, grade))
        conn.commit()
    except Error as e:
        st.error(f"新增失敗：{e}")
    cursor.close()
    conn.close()

def update_student(std_id, name, age, dept, signin, grade):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE ksu_std_table SET ksu_std_name=%s, ksu_std_age=%s, ksu_std_department=%s, ksu_std_signin=%s, ksu_std_grade=%s WHERE ksu_std_id=%s",
                       (name, age, dept, signin, grade, std_id))
        conn.commit()
    except Error as e:
        st.error(f"修改失敗：{e}")
    cursor.close()
    conn.close()

def delete_student(std_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM ksu_std_table WHERE ksu_std_id = %s", (std_id,))
        conn.commit()
    except Error as e:
        st.error(f"刪除失敗：{e}")
    cursor.close()
    conn.close()

st.title("KSU 學生資料管理系統")

menu = ["查詢全部", "新增學生", "修改學生", "刪除學生"]
choice = st.sidebar.selectbox("操作選單", menu)

if choice == "查詢全部":
    st.subheader("查詢學生資料")
    df = fetch_all_students()
    st.dataframe(df)

elif choice == "新增學生":
    st.subheader("新增學生資料")
    std_id = st.text_input("學號 (最多 6 碼)")
    name = st.text_input("姓名")
    age = st.number_input("年齡", min_value=0, max_value=120)
    dept = st.text_input("科系代碼")
    signin = st.date_input("註冊日期")
    grade = st.number_input("成績", min_value=0, max_value=100)

    if st.button("新增"):
        if not std_id.strip():
            st.error("請輸入學號")
        elif len(std_id.strip()) > 6:
            st.error("學號長度不得超過 6 碼")
        elif student_exists(std_id.strip()):
            st.error("此學號已存在")
        elif not name.strip():
            st.error("請輸入姓名")
        elif age <= 0:
            st.error("年齡需大於 0")
        elif not dept.strip():
            st.error("請輸入科系代碼")
        else:
            insert_student(std_id.strip(), name.strip(), age, dept.strip(), signin.strftime('%Y-%m-%d'), grade)
            st.success("✅ 新增成功！")

elif choice == "修改學生":
    st.subheader("修改學生資料")
    std_id = st.text_input("輸入欲修改的學號")
    name = st.text_input("新姓名 (選填)")
    age = st.text_input("新年齡 (整數)")
    dept = st.text_input("新科系代碼 (選填)")
    signin = st.text_input("新註冊日期 (YYYY-MM-DD)")
    grade = st.text_input("新成績 (0~100)")

    if st.button("修改"):
        errors = []

        if not std_id.strip():
            errors.append("請輸入學號")
        elif len(std_id.strip()) > 6:
            errors.append("學號長度不得超過 6 碼")
        elif not student_exists(std_id.strip()):
            errors.append("查無此學號")

        if age:
            if not age.isdigit() or not (1 <= int(age) <= 120):
                errors.append("年齡需為 1~120 的整數")
        if grade:
            if not grade.isdigit() or not (0 <= int(grade) <= 100):
                errors.append("成績需為 0~100 的整數")
        if signin:
            try:
                pd.to_datetime(signin)
            except:
                errors.append("註冊日期格式錯誤，請用 YYYY-MM-DD")

        if errors:
            for err in errors:
                st.error(err)
            st.stop()

        orig = get_student_by_id(std_id.strip())
        final_name = name.strip() if name.strip() else orig[1]
        final_age = int(age) if age else orig[2]
        final_dept = dept.strip() if dept.strip() else orig[3]
        final_signin = pd.to_datetime(signin).strftime("%Y-%m-%d") if signin else orig[4]
        final_grade = int(grade) if grade else orig[5]

        update_student(std_id.strip(), final_name, final_age, final_dept, final_signin, final_grade)
        st.success("✅ 修改成功！")

elif choice == "刪除學生":
    st.subheader("刪除學生資料")
    std_id = st.text_input("輸入欲刪除的學號")
    if st.button("刪除"):
        if not std_id.strip():
            st.error("請輸入學號")
        elif not student_exists(std_id.strip()):
            st.error("查無此學號")
        else:
            delete_student(std_id.strip())
            st.success("✅ 刪除成功！")