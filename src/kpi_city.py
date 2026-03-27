import sqlite3
import os

def city_kpi(city: str):
    db_path = os.path.join('data', 'db', 'analytics.db')
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    query = """
    SELECT 
        COUNT(*) as total_customers,
        AVG(monthly_spend) as avg_monthly_spend,
        SUM(churned) as churned_customers,
        ROUND(SUM(churned) * 100.0 / COUNT(*), 2) as churn_rate_pct
    FROM customers_raw 
    WHERE city = ?
    """
    
    cursor.execute(query, (city,))
    result = cursor.fetchone()
    conn.close()
    
    if result and result[0] > 0:
        total_customers, avg_spend, churned_customers, churn_rate = result
        print(f"KPI for {city}:")
        print(f"  Total Customers: {total_customers}")
        print(f"  Avg Monthly Spend: ${avg_spend:.2f}")
        print(f"  Churned Customers: {churned_customers}")
        print(f"  Churn Rate: {churn_rate}%")
    else:
        print(f"No data found for city: {city}")

if __name__ == "__main__":
    city_kpi("Mumbai")
    city_kpi("Mumbai' OR 1=1 --")
