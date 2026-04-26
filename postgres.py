import pandas as pd

import psycopg2
df_results = pd.read_csv(r"C:\Users\Urvi Patel\customer-intelligence-system\data\processed\churn_results.csv")
conn = psycopg2.connect(
    dbname="churn_db",
    user="postgres",
    password="postgres123",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# insert data row by row
for _, row in df_results.iterrows():
    cursor.execute("""
        INSERT INTO churn_data 
        (probability, prediction, actual, risk_segment, action, group_name, converted)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        float(row['probability']),
        int(row['prediction']),
        int(row['actual']),
        row['risk_segment'],
        row['action'],
        row['group_name'],
        int(row['converted'])
    ))

conn.commit()
cursor.close()
conn.close()

print("✅ Data inserted successfully")