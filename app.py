# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p0OeyePF-K_xkdHO0h3lnyx6HpbUX_6l
"""

import streamlit as st
import pandas as pd
import pickle

# Load model AI
@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Fungsi prediksi
def predict(model, data):
    predictions = model.predict(data)
    return predictions

# Judul aplikasi
st.title("Prediksi Model Machine Learning dengan Data Excel")

# Upload file Excel
uploaded_file = st.file_uploader("Upload file Excel", type=["xlsx", "xls"])

if uploaded_file:
    # Membaca file Excel
    data = pd.read_excel(uploaded_file)
    st.write("Data yang diunggah:")
    st.write(data)

    # Load model
    model = load_model()

    # Prediksi
    if st.button("Prediksi"):
        try:
            predictions = predict(model, data)
            data['Prediction'] = predictions
            st.success("Prediksi berhasil!")
            st.write("Hasil Prediksi:")
            st.write(data)
        except Exception as e:
            st.error(f"Error: {e}")

    # Tombol untuk mengunduh hasil prediksi
    if 'Prediction' in data.columns:
        st.download_button(
            label="Unduh Hasil Prediksi",
            data=data.to_csv(index=False).encode('utf-8'),
            file_name='hasil_prediksi.csv',
            mime='text/csv'
        )