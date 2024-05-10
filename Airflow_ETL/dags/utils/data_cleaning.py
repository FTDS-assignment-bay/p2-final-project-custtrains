# LIbrary
import pandas as pd
import numpy as np
from datetime import datetime
from feature_engine.outliers import Winsorizer

def clean_data():
  '''
  Fungsi ini bertujuan untuk melakukan preprocessing data/ data cleaning pada file csv dari PostgreSQL yang terbentuk dan memasukkan data hasil cleaning tersebut kedalam file csv baru.
  '''

  # Load CSV File
  current_date = datetime.now().strftime("%Y-%m-%d")
  data = pd.read_csv(f'/opt/airflow/data/customer_{current_date}_data.csv')

  # Drop Column_ID
  data.drop('Customer_ID', axis=1, inplace=True)

  # drop data yang memiliki frequency of purchases annually, every 3 months, dan quarterly karna data yang dibutuhkan hanya yang terjadi setiap 1 bulan
  data = data.drop(data[(data['Frequency of Purchases'] == 'Annually') |
                  (data['Frequency of Purchases'] == 'Every 3 Months') |
                  (data['Frequency of Purchases'] == 'Quarterly')].index)

  # Drop duplicates
  data.drop_duplicates(inplace=True)

  # Handling missing value
  data = data.dropna()

  # mengelompokan kolom
  numerik = data.select_dtypes(exclude=['object', 'datetime64']).columns.tolist()

  winsoriser = Winsorizer(capping_method='gaussian',
                            tail='both',
                            fold=3,
                            variables=numerik,
                            missing_values='ignore')

  data_capped = winsoriser.fit_transform(data)

  # Save File to CSV
  data_capped.to_csv(f'/opt/airflow/data/customer_{current_date}_data_clean.csv', index=False)