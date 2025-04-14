# KSU 學生資料管理系統

本專案為崑山科技大學課程期中報告，使用 Python 的 Streamlit 框架與 MySQL 資料庫開發的學生資料管理系統。

---

## 📌 專案簡介

本系統為 Web 應用程式，整合 MySQL 資料庫進行學生資料管理。允許使用者對學生記錄進行完整的 CRUD（新增、查詢、更新、刪除）操作，並具備欄位驗證、防呆與條件查詢功能。

---

## 🧩 功能特點

- ✅ **查詢全部學生**：以表格顯示所有學生資料，支援條件過濾
- ➕ **新增學生**：驗證輸入資料（學號、姓名、年齡等）後建立新學生記錄
- 📝 **修改學生**：支援部分欄位更新，未輸入欄位將保留原值
- ❌ **刪除學生**：依學號刪除指定學生資料

---

## ⚙️ 使用技術

- 前端框架：Streamlit
- 資料庫：MySQL（建議搭配 XAMPP）
- 資料連接：mysql-connector-python
- 資料處理：pandas

---

## 📁 專案結構

```
ksu-student-manager/
├─ main.py                  # 主程式（Streamlit + CRUD 操作）
├─ requirements.txt         # 套件需求清單
└─ README.md                # 專案說明文件

```

---

## 🗂 資料表欄位（ksu_std_table）

| 欄位名稱           | 資料類型    | 描述             |
|--------------------|-------------|------------------|
| ksu_std_id         | VARCHAR(6)  | 學號（主鍵）     |
| ksu_std_name       | VARCHAR(50) | 學生姓名         |
| ksu_std_age        | INT         | 年齡             |
| ksu_std_department | VARCHAR(50) | 科系代碼         |
| ksu_std_signin     | DATE        | 註冊日期         |
| ksu_std_grade      | INT         | 學生成績         |

---

## 🧪 資料驗證規則

- 學號為必填且長度不超過 6 碼
- 姓名不得為空
- 年齡為 1～120 的正整數
- 成績為 0～100 的整數
- 註冊日期格式須為 YYYY-MM-DD

---

## 🚀 如何執行

1. 匯入提供的 SQL 資料表（`ksu_database`）至本地 MySQL
2. 安裝依賴套件：
```bash
pip install -r requirements.txt
```
3. 執行系統：
```bash
streamlit run main.py
```
4. 使用側邊欄選單進行操作

---

