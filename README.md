# KSU 學生資料管理系統 (期中專案)

🎓 本專案為崑山科技大學「資料庫應用與網頁開發」課程期中報告。目標為建立一套具備 CRUD 功能的學生資料管理平台，採用 Python Streamlit 建立前端互動介面，MySQL 作為後端資料庫，並支援即時查詢、自動補全、欄位驗證與錯誤提示。

🧪 系統採 MVC 架構（Model: 資料層函式 / Controller: 控制流程 / View: 使用者介面），具備可讀性與模組化擴充潛力。

---

## 🔧 技術與架構

- Python 3.11
- Streamlit 1.31
- MySQL 8 (搭配 XAMPP)
- mysql-connector-python
- pandas (主要用於顯示表格)
- 架構模式：MVC
  - Model：可封裝為 db.py
  - Controller/View：main.py

---

## ✨ 功能說明

- 查詢學生：支援依條件過濾顯示學生資料
- 新增學生：學號唯一、長度限制，姓名、年齡、科系皆驗證
- 修改學生：欄位留空則保留原值
- 刪除學生：依學號刪除紀錄
- 錯誤提示：欄位錯誤即時以紅框顯示
- 表格即時更新：資料操作完即更新畫面

---

## 📏 資料驗證規則

- 學號：不超過 6 碼、不可重複
- 姓名與科系代碼：不可空白
- 年齡：1~120
- 成績：0~100
- 註冊日期：YYYY-MM-DD 格式

---

## 🧱 資料庫設計（ERD）

本系統使用單一學生資料表：`ksu_std_table`，資料結構如下：

| 欄位名稱           | 資料型別    | 說明           |
|--------------------|-------------|----------------|
| ksu_std_id         | VARCHAR(6)  | 學號，主鍵     |
| ksu_std_name       | VARCHAR(50) | 姓名           |
| ksu_std_age        | INT         | 年齡           |
| ksu_std_department | VARCHAR(50) | 科系代碼       |
| ksu_std_signin     | DATE        | 註冊日期       |
| ksu_std_grade      | INT         | 成績 (0~100)   |

---

## 🚀 專案啟動方式

1. 安裝依賴：
```bash
pip install -r requirements.txt
```

2. 匯入資料庫：
```bash
mysql -u root -p
CREATE DATABASE ksu_database;
USE ksu_database;
SOURCE ksu_database_20210914_full.sql;
```

3. 執行應用：
```bash
streamlit run main.py
```

---

## 🔮 後續擴充計畫

- 增加登入機制（預計實作 JWT 認證）
- 多資料表關聯（課程、教師、修課紀錄）
- 權限控管與分頁查詢

---
