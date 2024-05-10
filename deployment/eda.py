import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    # Set title
    st.title('Exploratory Data Analysis Page')
    st.image('image1.jpg', use_column_width=True)
    
    # Load data
    dfEDA2 = pd.read_csv('unsupervised_data.csv')

    st.header('Perbandingan Penggunaan Promo Code Berdasarkan Cluster')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x='Promo Code Used', hue='Cluster', data=dfEDA2, palette='viridis', ax=ax)
    plt.title('Frequency of Purchases by Promo Code Used and Frequency')
    plt.xlabel('Discount Promo Code Used')
    plt.ylabel('Frequency of Purchases')
    st.pyplot(fig)

    # Plot 
    st.header('Perbandingan Pengguna Jenis Pengiriman Berdasarkan Cluster')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x='Shipping Type', hue='Cluster', data=dfEDA2, palette='viridis', ax=ax)
    plt.title('Frequency of Purchases by Shipping Type and Frequency')
    plt.xlabel('Shipping Type')
    plt.ylabel('Frequency of Purchases')
    st.pyplot(fig)

    # Plot 
    st.header('Perbandingan Subscription Status Berdasarkan Cluster')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x='Subscription Status', hue='Cluster', data=dfEDA2, palette='viridis', ax=ax)
    plt.title('Frequency of Purchases by Subscription Status and Frequency')
    plt.xlabel('Subscription Status')
    plt.ylabel('Frequency of Purchases')
    st.pyplot(fig)

    # Plot 
    st.header('Perbandingan Category Berdasarkan Cluster')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x='Category', hue='Cluster', data=dfEDA2, ax=ax)
    plt.title('Category by Cluster')
    plt.tight_layout()
    st.pyplot(fig)

    st.header("""Heatmap Semua Kolom Dengan Cluster""")
    # Heatmap atau stacked bar chart untuk variabel kategorikal
    for kol in dfEDA2.columns.tolist():
        contingency_table = pd.crosstab(dfEDA2['Cluster'], dfEDA2[kol])
        fig, ax = plt.subplots(figsize=(20, 10))
        sns.heatmap(contingency_table, annot=True, cmap='coolwarm', ax=ax)
        plt.title(f'Correlation Heatmap of {kol} and Cluster')
        plt.xlabel(kol)
        plt.ylabel('Cluster')
        st.pyplot(fig)

if __name__ == "__main__":
    app()
