import pandas as pd
import streamlit as st
import pickle as pkl
import json as js
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    with open('list_kolom_numerik.txt', 'r') as num:
        numeric = js.load(num)
    with open('list_kolom_kategorik.txt', 'r') as cat:
        categoric = js.load(cat)
    with open('modelBest.pkl', 'rb') as file:
        model = pkl.load(file)
    
    st.title('Silahkan Periksa Kategori Customer Anda!')
    # Menampilkan gambar
    st.image('image2.jpg', use_column_width=True)
    
    with st.form('Input Data Pelanggan'):

        uploaded_file = st.file_uploader("Choose a file")

        submit_button = st.form_submit_button('Submit Data')

    if submit_button:

        listKolom = numeric + categoric

        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
        else:
            st.error('Failed to load file')

        if df is None:
            st.error('Failed to load data')
        else:
            df.drop(columns=[col for col in df.columns if col not in listKolom], inplace=True)

            modelPred = model.predict(df)

            label = []

            for val in modelPred:
                if val == 0:
                    label.append("Discount Hunter")
                elif val == 1:
                    label.append("Royal Customer")
                elif val == 2:
                    label.append("Normal Customer")
                else:
                    label.append("Loyal Customer")
            
            dfPred = df.copy()
            dfPred['Cluster'] = label
            st.write(dfPred)

            st.header('Perbandingan Penggunaan Promo Code Berdasarkan Cluster')
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.countplot(x='Promo Code Used', hue='Cluster', data=dfPred, palette='viridis', ax=ax)
            plt.title('Frequency of Purchases by Promo Code Used and Frequency')
            plt.xlabel('Discount Promo Code Used')
            plt.ylabel('Frequency of Purchases')
            st.pyplot(fig)

            # Plot 
            st.header('Perbandingan Pengguna Jenis Pengiriman Berdasarkan Cluster')
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.countplot(x='Shipping Type', hue='Cluster', data=dfPred, palette='viridis', ax=ax)
            plt.title('Frequency of Purchases by Shipping Type and Frequency')
            plt.xlabel('Shipping Type')
            plt.ylabel('Frequency of Purchases')
            st.pyplot(fig)

            st.header('Perbandingan Category Berdasarkan Cluster')
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.countplot(x='Category', hue='Cluster', data=dfPred, ax=ax)
            plt.title('Category by Cluster')
            plt.tight_layout()
            st.pyplot(fig)

            csv = dfPred.to_csv(index=False).encode('utf-8')

            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='cluster_data.csv',
                mime='text/csv'
            )
        

if __name__ == "__main__":
    app()
