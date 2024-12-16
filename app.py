import streamlit as st
from tensorflow.keras.models import load_model
import pandas as pd

# Fungsi untuk load model Keras
@st.cache_resource
def load_model_keras():
    model = load_model("model.keras")  # Pastikan file 'model.keras' ada di direktori yang sama
    return model

# Load model
model = load_model_keras()

# Judul aplikasi
st.title("Prediksi Model Machine Learning dengan Data Excel")

# Upload file Excel
uploaded_file = st.file_uploader("Upload file Excel", type=["xlsx", "xls"])

if uploaded_file:
    try:
        # Membaca data Excel
        data = pd.read_excel(uploaded_file)
        st.write("Data yang diunggah:")
        st.write(data)

        # Tombol untuk prediksi
        if st.button("Prediksi"):
            # Pastikan format input sesuai dengan model
            predictions = model.predict(data)
            data['Prediction'] = predictions.argmax(axis=1)  # Jika model klasifikasi multi-kelas

            st.success("Prediksi berhasil!")
            st.write("Hasil Prediksi:")
            st.write(data)

            # Tombol unduh hasil prediksi
            st.download_button(
                label="Unduh Hasil Prediksi",
                data=data.to_csv(index=False).encode('utf-8'),
                file_name="hasil_prediksi.csv",
                mime="text/csv"
            )
    except Exception as e:
        st.error(f"Error: {e}")
