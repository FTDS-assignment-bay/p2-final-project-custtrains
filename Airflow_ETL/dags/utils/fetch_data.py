# Library
import pandas as pd
from datetime import datetime
import psycopg2 as db

def fetch_data_from_postgres():
    '''
    Fungsi ini bertujuan untuk mengambil data dari table di PostgreSQL dan memasukkannya kedalam sebuah file csv.
    '''
    # Fetch Data using psycopg2
    database = "customer_data"
    conn_string=(f"dbname='{database}' host='postgres' user='postgres' password='postgres' port='5432'")
    try:
        conn=db.connect(conn_string)
        # df=pd.read_sql("select * from shopping_behavior", conn)
        df=pd.read_sql('''SELECT * FROM customer WHERE "Date" >= date_trunc('month', CURRENT_DATE) - interval '1 month' AND "Date" < date_trunc('month', CURRENT_DATE)''', conn)
        # df.to_csv('fetchData.csv',index=False)

        # Save File
        current_date = datetime.now().strftime("%Y-%m-%d")
        df.to_csv(f'/opt/airflow/data/customer_{current_date}_data.csv', sep=',', index=False)

    except Exception as e:
        print(f"Connection failed: {e}")

    