import pytest
import sqlite3
import os
import sys
from io import StringIO
from unittest.mock import patch

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from kpi_city import city_kpi

@pytest.fixture
def setup_test_db():
    db_path = os.path.join('data', 'db', 'analytics.db')
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM customers_raw")
    
    test_data = [
        (1, 'Mumbai', 1500.50, 0),
        (2, 'Mumbai', 800.25, 1),
        (3, 'Delhi', 2300.75, 0),
        (4, 'Mumbai', 4500.25, 0)
    ]
    
    cursor.executemany(
        "INSERT INTO customers_raw (customer_id, city, monthly_spend, churned) VALUES (?, ?, ?, ?)",
        test_data
    )
    
    conn.commit()
    conn.close()
    
    yield
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customers_raw")
    conn.commit()
    conn.close()

def test_city_kpi_happy_path(setup_test_db):
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        city_kpi("Mumbai")
        output = mock_stdout.getvalue()
    
    assert "KPI for Mumbai:" in output
    assert "Total Customers: 3" in output
    assert "Churned Customers: 1" in output
    assert "Churn Rate: 33.33%" in output

def test_city_kpi_sql_injection_attempt(setup_test_db):
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        city_kpi("Mumbai' OR 1=1 --")
        output = mock_stdout.getvalue()
    
    assert "No data found for city: Mumbai' OR 1=1 --" in output
    assert "Total Customers: 4" not in output
