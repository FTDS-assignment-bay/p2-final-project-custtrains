import pandas as pd
from datetime import datetime, timedelta
import psycopg2 as db

def load_csv_to_postgres():
    '''
    Fungsi ini bertujuan untuk mengunggah data clustering ke PostgreSQL.
    '''

    database = "customer_data"

    conn_string=(f"dbname='{database}' host='postgres' user='postgres' password='postgres' port='5432'")
    try:
        # Connect to PostgreSQL
        conn=db.connect(conn_string)
        cur = conn.cursor()

        # Save File to Database
        
        called_date = datetime.now() - timedelta(days=7)
        formatted_date = called_date.strftime("%Y-%m-%d")

        current_date = datetime.now().strftime("%Y-%m-%d")
        query = '''COPY customer_cluster 
                        FROM stdin
                        with
                        CSV HEADER
                        DELIMITER as ',' '''
        filePath = f'/opt/airflow/data/customer_{current_date}_data_cluster.csv'
        
        with open(filePath, 'r') as upload:
             cur.copy_expert(sql=query, file=upload)
        
        conn.commit()

        cur.close()
        conn.close()
            
    except Exception as e:
            print(f"Connection failed: {e}")