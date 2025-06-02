import streamlit as st
import joblib
import pandas as pd

# Load model dan encoders
with open('model/rf_model.joblib', 'rb') as model_file:
    model = joblib.load(model_file)
with open('model/preprocessing.joblib', 'rb') as le_file:
    preprocessing = joblib.load(le_file)
with open('model/label_encoder.joblib', 'rb') as le_file:
    label_encoder = joblib.load(le_file)

preprocessor = preprocessing['preprocessor']
categorical_features = preprocessing['categorical_features']
numerical_features = preprocessing['numerical_features']

st.title("Prediksi Status Mahasiswa")

name = st.text_input("Nama Lengkap", "")

gender = st.selectbox(
    "Jenis Kelamin",
    ("Laki-laki", "Perempuan")
)

age_at_enrollment = st.number_input("Usia Saat Mendaftar")

course = st.selectbox(
    "Program Studi",
    ("Biofuel Production Technologies", "Animation and Multimedia Design", "Social Service (evening attendance)",
     "Agronomy", "Communication Design", "Veterinary Nursing", "Informatics Engineering", "Equinculture", "Management",
     "Social Service", "Tourism", "Nursing", "Oral Hygiene", "Advertising and Marketing Management",
     "Journalism and Communication", "Basic Education", "Management (evening attendance)")
)

app_mode = st.selectbox(
    "Jalur Masuk",
    ("1st phase - general contingent", "Ordinance No. 612/93", "1st phase - special contingent (Azores Island)", "Holders of other higher courses",
     "Ordinance No. 854-B/99", "International student (bachelor)", "1st phase - special contingent (Madeira Island)",
     "2nd phase - general contingent", "3rd phase - general contingent", "Ordinance No. 533-A/99, item b2 (Different Plan)",
     "Ordinance No. 533-A/99, item b3 (Other Institution)", "Over 23 years old", "Transfer", "Change of course", "Technological specialization diploma holders",
     "Change of institution/course", "Short cycle diploma holders", "Change of institution/course (International)")
)

app_order = st.selectbox(
    "Application Order",
    ("1", "2", "3", "4", "5", "6", "7", "8", "9")
)

marital_status = st.selectbox(
    "Status Pernikahan",
    ("Lajang", "Menikah", "Duda", "Bercerai",
    "Bersatu secara fakto", "Berpisah secara hukum")
)

tuition_fees_up_to_date = st.radio(
    "UKT Terbaru",
    ("Ya", "Tidak"),
    index=None,
    horizontal=True
)

scholarship_holder = st.radio(
    "Penerima Beasiswa",
    ("Ya", "Tidak"),
    index=None,
    horizontal=True
)

debtor = st.radio(
    "Melakukan Pinjaman",
    ["Ya", "Tidak"],
    index=None,
    horizontal=True
)

daytime_evening_attendance = st.radio(
    "Mengambil Kelas Siang/Malam",
    ["Siang", "Malam"],
    index=None,
    horizontal=True
)

curricular_units_1st_sem_approved = st.slider("SKS yang Disetujui oleh Mahasiswa di Semester 1", 0, 24, 17)

curricular_units_2nd_sem_approved = st.slider("SKS yang Disetujui oleh Mahasiswa di Semester 1", 0, 24, 17)

first_sem_grade = st.number_input("IP Semester 1")
if not 0 <= first_sem_grade <= 4:
    st.warning("IP Semester 1 harus antara 0 dan 4.")

sec_sem_grade = st.number_input("IP Semester 2")
if not 0 <= sec_sem_grade <= 4:
    st.warning("IP Semester 2 harus antara 0 dan 4.")

avg_grade = st.number_input("IPK", min_value=0.00, max_value=4.00)
if not 0 <= avg_grade <= 4:
    st.warning("IPK harus antara 0 dan 4.")


predict = st.button("Predict Status")

if predict:
    # Menyiapkan data input
    input_data = {
        'Marital_status': marital_status,
        'Application_mode': app_mode,
        'Application_order': int(app_order),
        'Course': course,
        'Daytime_evening_attendance': daytime_evening_attendance,
        'Age_at_enrollment': age_at_enrollment,
        'Curricular_units_1st_sem_approved': curricular_units_1st_sem_approved,
        'Curricular_units_2nd_sem_approved': curricular_units_2nd_sem_approved,
        'Debtor': debtor,
        'Tuition_fees_up_to_date': tuition_fees_up_to_date,
        'Gender': gender,
        'Scholarship_holder': scholarship_holder,
        'Curricular_units_1st_sem_grade': first_sem_grade,
        'Curricular_units_2nd_sem_grade': sec_sem_grade,
        'avg_grade': avg_grade
    }
    
    # Konversi ke DataFrame
    input_df = pd.DataFrame([input_data])

    # Transformasi input
    input_df = input_df[categorical_features + numerical_features]
    input_transformed = preprocessor.transform(input_df)
    input_array = input_transformed.toarray()

    # Prediksi
    prediction = model.predict(input_array)
    prediction_proba = model.predict_proba(input_array)

    # Mapping label
    predicted_label = label_encoder.inverse_transform(prediction)

    st.success(f"Hasil Prediksi: {predicted_label[0]}")
    