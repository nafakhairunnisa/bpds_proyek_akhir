import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load model dan encoders
with open('best_model.joblib', 'rb') as model_file:
    model = joblib.load(model_file)
with open('preprocessing_components.joblib', 'rb') as le_file:
    preprocessing = joblib.load(le_file)

st.title("Prediksi Status Mahasiswa")

st.text_input("Nama Lengkap", "")

gender = st.selectbox(
    "Jenis Kelamin",
    ("Laki-laki", "Perempuan")
)

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

mothers_qualification = st.selectbox(
    "Pendidikan Ibu",
    [
        "Pendidikan Menengah - Tahun ke-12 Sekolah atau Setara",
        "Pendidikan Tinggi - Gelar Sarjana",
        "Pendidikan Tinggi - Gelar Master",
        "Pendidikan Tinggi - Doktor",
        "Frekuensi Pendidikan Tinggi",
        "Tahun ke-12 Sekolah - Tidak Tamat",
        "Tahun ke-11 Sekolah - Tidak Tamat",
        "Tahun ke-7 (Tua)",
        "Lainnya - Tahun ke-11 Sekolah",
        "Tahun ke-10 Sekolah",
        "Kursus perdagangan umum",
        "Pendidikan Dasar Siklus ke-3 (Tahun ke-9 / 10 / 11) atau Setara",
        "Kursus teknis-profesional",
        "Tahun ke-7 sekolah",
        "Siklus ke-2 sekolah menengah umum",
        "Tahun ke-9 sekolah - Tidak Tamat",
        "Tahun ke-8 sekolah",
        "Tidak diketahui",
        "Tidak dapat membaca atau menulis",
        "Dapat membaca tanpa sekolah tahun ke-4",
        "Pendidikan dasar siklus pertama (tahun ke-4 / 5) atau setara",
        "Pendidikan dasar siklus ke-2 (tahun ke-6/7/8) atau sederajat",
        "Kursus spesialisasi teknologi",
        "Pendidikan tinggi - sarjana (siklus ke-1)",
        "Kursus spesialisasi pendidikan tinggi",
        "Kursus teknis profesional yang lebih tinggi",
        "Pendidikan tinggi - Master (siklus ke-2)",
        "Pendidikan tinggi - Doktor (siklus ke-3)"
    ]
)

fathers_qualification = st.selectbox(
    "Pendidikan Ayah",
    [
        "Pendidikan Menengah - Tahun ke-12 Sekolah atau Setara",
        "Pendidikan Tinggi - Gelar Sarjana",
        "Pendidikan Tinggi - Gelar Magister",
        "Pendidikan Tinggi - Gelar Doktor",
        "Frekuensi Pendidikan Tinggi",
        "Tahun ke-12 Sekolah - Tidak Selesai",
        "Tahun ke-11 Sekolah - Tidak Selesai",
        "Tahun ke-7 (Tua)",
        "Lainnya - Tahun ke-11 Sekolah",
        "Kursus Sekolah Menengah Pelengkap tahun ke-2",
        "Tahun ke-10 Sekolah",
        "Kursus Perdagangan Umum",
        "Pendidikan Dasar Siklus ke-3 (Tahun ke-9 / 10 / 11) atau Setara",
        "Kursus Pelengkap Sekolah Menengah Atas",
        "Kursus Teknis-Profesional",
        "Kursus Pelengkap Sekolah Menengah Atas - tidak selesai",
        "Tahun ke-7 sekolah",
        "Siklus ke-2 kursus sekolah menengah umum",
        "Tahun ke-9 sekolah - tidak selesai",
        "Tahun ke-8 sekolah",
        "Kursus Umum Administrasi dan Perdagangan",
        "Akuntansi dan Administrasi Tambahan",
        "Tidak diketahui",
        "Tidak dapat membaca atau menulis",
        "Dapat membaca tanpa harus bersekolah di tahun ke-4",
        "Pendidikan Dasar Siklus ke-1 (tahun ke-4/5) atau setara",
        "Pendidikan dasar siklus ke-2 (tahun ke-6/7/8) atau sederajat",
        "Kursus spesialisasi teknologi",
        "Pendidikan tinggi - sarjana (siklus ke-1)",
        "Kursus spesialisasi pendidikan tinggi",
        "Kursus teknis profesional yang lebih tinggi",
        "Pendidikan tinggi - Master (siklus ke-2)",
        "Pendidikan tinggi - Doktor (siklus ke-3)"
    ]
)

sec_sem_enrolled = st.slider("SKS Terdaftar di Semester 2", 0, 24, 17)

first_sem_grade = st.number_input("IP Semester 1")
sec_sem_grade = st.number_input("IP Semester 2")

avg_grade = st.number_input("IPK", min_value=0.00, max_value=4.00)


predict = st.button("Predict Status")

if predict:
    # Prepare input data
    input_data = {
        'Gender': gender,
        'Course': course,
        'Application_mode': app_mode,
        'Tuition_fees_up_to_date': tuition_fees_up_to_date,
        'Scholarship_holder': scholarship_holder,
        'Debtor': debtor,
        'Mothers_qualification': mothers_qualification,
        'Fathers_qualification': fathers_qualification,
        'Curricular_units_2nd_sem_enrolled': sec_sem_enrolled,
        'Curricular_units_1st_sem_grade': first_sem_grade,
        'Curricular_units_2nd_sem_grade': sec_sem_grade,
        'avg_grade': avg_grade
    }
    
    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Transform categorical features using preprocessing components
    categorical_features = ['Gender', 'Course', 'Application_mode', 'Tuition_fees_up_to_date', 
                          'Scholarship_holder', 'Debtor', 'Mothers_qualification', 'Fathers_qualification']
    
    for feature in categorical_features:
        if feature in preprocessing:
            le = preprocessing[feature]
            input_df[feature] = le.transform(input_df[feature])
    
    # Make prediction
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)
    
    # Display results
    st.write("---")
    st.subheader("Hasil Prediksi")
    
    if prediction[0] == 1:
        st.error("Mahasiswa berisiko Dropout")
    else:
        st.success("Mahasiswa tidak berisiko Dropout")
    
    # Show probability
    dropout_prob = prediction_proba[0][1] * 100
    st.write(f"Probabilitas Dropout: {dropout_prob:.2f}%")
    
    # Show feature importance if available
    if hasattr(model, 'feature_importances_'):
        st.subheader("Faktor yang Mempengaruhi")
        feature_importance = pd.DataFrame({
            'Fitur': input_df.columns,
            'Penting': model.feature_importances_
        })
        feature_importance = feature_importance.sort_values('Penting', ascending=False)
        st.bar_chart(feature_importance.set_index('Fitur'))

