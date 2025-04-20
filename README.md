# KSU 學生資料管理系統

本專案為崑山科技大學課程期中報告，使用 Python 的 Streamlit 框架與 MySQL 資料庫開發的學生資料管理系統。

---

## 📌 專案簡介

本系統為 Web 應用程式，整合 MySQL 資料庫進行學生資料管理，支援以下功能：

- 新增學生資料（含欄位驗證）
- 查詢全部學生資料（支援條件過濾）
- 修改學生資料（可只改部分欄位）
- 刪除學生資料

---

## 🧩 功能模組

| 模組功能 | 說明 |
|----------|------|
| 查詢學生 | 顯示所有學生，支援依條件篩選 |
| 新增學生 | 檢查欄位正確性後新增學生 |
| 修改學生 | 只更新有填寫的欄位，其他保留原值 |
| 刪除學生 | 根據學號刪除學生記錄 |

---

## 🧱 資料庫結構（ERD）

資料表名稱：`ksu_std_table`

| 欄位名稱           | 資料類型    | 說明           |
|--------------------|-------------|----------------|
| `ksu_std_id`       | VARCHAR(6)  | 學號，主鍵     |
| `ksu_std_name`     | VARCHAR(50) | 學生姓名       |
| `ksu_std_age`      | INT         | 學生年齡       |
| `ksu_std_department` | VARCHAR(50)| 科系代碼       |
| `ksu_std_signin`   | DATE        | 註冊日期       |
| `ksu_std_grade`    | INT         | 成績 (0~100)   |

---

## 🧪 資料驗證規則

- 學號：長度不超過 6 碼，不能重複
- 姓名：不可為空
- 年齡：1~120 間整數
- 科系代碼：不可為空
- 成績：0~100 整數
- 註冊日期：符合 `YYYY-MM-DD` 格式

---

## 🚀 如何執行

1. 安裝套件：
```bash
pip install -r requirements.txt
```

2. 匯入 MySQL 資料庫（使用提供的 `.sql` 檔）：

   - 使用 phpMyAdmin 或
   ```bash
   mysql -u root -p ksu_database < ksu_database_20210914_full.sql
   ```

3. 執行程式：
```bash
streamlit run main.py
```

---

## 📂 專案結構

```
ksu-student-manager/
├─ main.py
├─ requirements.txt
├─ ksu_database_20210914_full.sql
└─ README.md
```

---

## 🧠 作者說明

本專案為課堂期中專案，後續將持續整理其他課程資料庫設計與系統功能擴充，如登入系統、多資料表設計等。

---