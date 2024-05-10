# Contents of main.py
import eda
import prediction
import predictionBatch
import streamlit as st
PAGES = {
    "EDA": eda,
    "Model Prediction": prediction,
    "Model Prediction Batch": predictionBatch
}
st.sidebar.title('Halaman')
selection = st.sidebar.radio("Pilih Halaman", list(PAGES.keys()))
page = PAGES[selection]
page.app()