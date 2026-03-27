# Applied Analytics Mini Project

A beginner-friendly project demonstrating data ETL, KPI calculations, and SQL injection protection.

## Project Structure
```
vibe-kpi-demo/
├── data/
│   ├── raw/customers_raw.csv     # Raw customer data
│   └── db/analytics.db           # SQLite database
├── src/
│   ├── etl_load_sqlite.py       # ETL script to load CSV to SQLite
│   └── kpi_city.py              # KPI calculation with SQL injection protection
├── tests/
│   └── test_kpi_city.py          # Pytest tests for KPI functions
├── requirements.txt              # Python dependencies
├── .gitignore                   # Git ignore file
└── README.md                    # This file
```

## Setup and Run Commands

### 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 2. Run ETL Script (Load CSV to SQLite)
```bash
python src/etl_load_sqlite.py
```

### 3. Run KPI Script
```bash
python src/kpi_city.py
```

### 4. Run Tests
```bash
pytest tests/test_kpi_city.py -v
```

## File Descriptions
- `data/raw/customers_raw.csv`: Sample customer data with 10 records across 4 cities
- `src/etl_load_sqlite.py`: Loads CSV data into SQLite database table
- `src/kpi_city.py`: Calculates city-specific KPIs using parameterized SQL queries
- `tests/test_kpi_city.py`: Tests for KPI function including SQL injection protection
- `requirements.txt`: Python package dependencies (pandas, pytest)
- `.gitignore`: Excludes virtual environment, cache, and database files
- `README.md`: Project documentation and setup instructions