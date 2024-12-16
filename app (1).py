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
    data = pd.read_excel(uploaded_file)
    st.write("Data yang diunggah:")
    st.write(data)

    model = load_model()

    if st.button("Prediksi"):
        try:
            predictions = predict(model, data)
            data['Prediction'] = predictions
            st.success("Prediksi berhasil!")
            st.write(data)
        except Exception as e:
            st.error(f"Error: {e}")
