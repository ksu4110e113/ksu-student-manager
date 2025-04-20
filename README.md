# KSU 學生資料管理系統 (期中專案)

🎓 本專案為崑山科技大學「資料庫應用與網頁開發」課程期中報告，旨在建立具備 **CRUD** 功能的學生資料管理平台。採用 **Python Streamlit** 打造互動介面，**MySQL** 作為後端資料庫，支援即時查詢、自動補全、欄位驗證與錯誤提示。

🧪 **GitHub**: https://github.com/ksu4110e113/ksu-student-manager\


## 🔧 技術棧

- Python 3.11
- Streamlit 1.31
- MySQL 8 (搭配 XAMPP)
- mysql-connector-python
- pandas
- 版本控制：Git

## ✨ 功能說明

- **查詢學生**：支援條件篩選（按姓名或學號），顯示動態表格。
- **新增學生**：驗證學號唯一性、年齡範圍等，確保資料正確性。
- **修改學生**：僅更新填寫欄位，保留其他欄位原值。
- **刪除學生**：依學號刪除記錄。
- **錯誤提示**：無效輸入顯示紅框警示。
- **UI 優化**：表單支援自動補全（科系代碼），表格操作後即時更新。

## 📏 資料驗證規則

- 學號：≤6 碼，唯一。
- 姓名、科系代碼：非空。
- 年齡：1\~120。
- 成績：0\~100。
- 註冊日期：YYYY-MM-DD 格式。

## 🧱 資料庫設計

單一資料表：`ksu_std_table`

| 欄位名稱 | 資料型別 | 說明 |
| --- | --- | --- |
| ksu_std_id | VARCHAR(6) | 學號，主鍵 |
| ksu_std_name | VARCHAR(50) | 姓名 |
| ksu_std_age | INT | 年齡 |
| ksu_std_department | VARCHAR(50) | 科系代碼 |
| ksu_std_signin | DATE | 註冊日期 |
| ksu_std_grade | INT | 成績 (0\~100) |

**Schema** (database/schema.sql):

```sql
CREATE TABLE ksu_std_table (
    ksu_std_id VARCHAR(6) PRIMARY KEY,
    ksu_std_name VARCHAR(50) NOT NULL,
    ksu_std_age INT CHECK (ksu_std_age BETWEEN 1 AND 120),
    ksu_std_department VARCHAR(50) NOT NULL,
    ksu_std_signin DATE,
    ksu_std_grade INT CHECK (ksu_std_grade BETWEEN 0 AND 100)
);
```

## 🚀 專案啟動方式

### Prerequisites

- Python 3.11+
- XAMPP (MySQL 8 enabled)
- Git

### Steps

1. **Clone 倉庫**:

   ```bash
   git clone https://github.com/ksu4110e113/ksu-student-manager.git
   cd ksu-student-manager
   ```
2. **安裝依賴**:

   ```bash
   pip install -r requirements.txt
   ```
3. **設置 MySQL**:
   - 啟動 XAMPP 和 MySQL。
   - 創建資料庫：

     ```bash
     mysql -u root -p
     CREATE DATABASE ksu_database;
     USE ksu_database;
     SOURCE database/schema.sql;
     ```
   - 或使用 phpMyAdmin 匯入 `schema.sql`。
4. **配置環境變數** (建議):
   - 創建 `.env`：

     ```env
     DB_USER=root
     DB_PASSWORD=
     DB_HOST=localhost
     DB_NAME=ksu_database
     ```
   - 在 `main.py` 使用 `python-dotenv` 載入憑證。
5. **執行應用**:

   ```bash
   streamlit run main.py
   ```
   - 瀏覽器開啟 `http://localhost:8501`。

## 📂 專案結構

```
ksu-student-manager/
├── main.py             # Streamlit 應用與資料庫操作
├── database/
│   └── schema.sql     # MySQL 表結構
├── requirements.txt   # 依賴
└── README.md          # 文件
```

## 📝 期中報告

本專案為課程期中作業，提交報告闡述系統架構、程式碼實現與學習成果。

## 🔮 後續計畫

- **認證**：實作 JWT 登入系統。
- **資料表**：新增課程、教師表，支援關聯查詢。
- **功能**：實現權限控管與分頁查詢。
- **部署**：上線至 Render，使用雲端 MySQL。

## ⚠️ 備註

- 學術專案，無真實學生資料。
- 建議使用環境變數保護 MySQL 憑證。
- 所有邏輯集中於 `main.py`，未來可優化結構。

## 📬 聯繫

- **姓名**：陳威任
- **Email**：e0916656088@gmail.com
- **GitHub**：ksu4110e113