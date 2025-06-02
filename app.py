import streamlit as st
import joblib
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Prediksi Status Mahasiswa",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# Load model dan encoders
try:
    with open('model/rf_model.pkl', 'rb') as model_file:
        model = joblib.load(model_file)
    with open('model/preprocessor.pkl', 'rb') as le_file:
        preprocessor = joblib.load(le_file)
    with open('model/label_encoder.pkl', 'rb') as le_file:
        label_encoder = joblib.load(le_file)

    # Mendapatkan categorical dan numerical features dari preprocessor
    categorical_features = preprocessor.named_transformers_['cat'].get_feature_names_out()
    numerical_features = preprocessor.named_transformers_['num'].get_feature_names_out()
except Exception as e:
    st.error(f"Error loading model files: {str(e)}")
    st.stop()

st.title("🎓 Prediksi Status Mahasiswa")
st.markdown("---")

# Input form
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Nama Lengkap", "")
        
        gender = st.selectbox(
            "Jenis Kelamin",
            ("Laki-laki", "Perempuan")
        )
        
        age_at_enrollment = st.number_input("Usia Saat Mendaftar", min_value=15, max_value=100)
        
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
            "Bersatu secara fakta", "Berpisah secara hukum")
        )
    
    with col2:
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
        
        curricular_units_2nd_sem_approved = st.slider("SKS yang Disetujui oleh Mahasiswa di Semester 2", 0, 24, 17)
        
        first_sem_grade = st.number_input("IP Semester 1", min_value=0.0, max_value=4.0, step=0.01)
        sec_sem_grade = st.number_input("IP Semester 2", min_value=0.0, max_value=4.0, step=0.01)
        avg_grade = st.number_input("IPK", min_value=0.0, max_value=4.0, step=0.01)

    predict = st.form_submit_button("Prediksi Status")

if predict:
    # Validasi input
    required_fields = {
        'Nama': name,
        'UKT Terbaru': tuition_fees_up_to_date,
        'Penerima Beasiswa': scholarship_holder,
        'Melakukan Pinjaman': debtor,
        'Kelas Siang/Malam': daytime_evening_attendance
    }
    
    missing_fields = [field for field, value in required_fields.items() if not value]
    
    if missing_fields:
        st.error(f"Mohon lengkapi field berikut: {', '.join(missing_fields)}")
    else:
        try:
            # Validasi nilai IP
            if not (0 <= first_sem_grade <= 4) or not (0 <= sec_sem_grade <= 4) or not (0 <= avg_grade <= 4):
                st.error("Nilai IP harus antara 0 dan 4")
                st.stop()

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
            input_transformed = preprocessor.transform(input_df)
            
            # Prediksi
            prediction = model.predict(input_transformed)
            
            # Mapping label
            predicted_label = label_encoder.inverse_transform(prediction)
            
            # Tampilkan hasil
            st.markdown("---")
            st.markdown("### Hasil Prediksi")
            
            # Tampilkan status dengan warna yang sesuai
            if predicted_label[0] == "Dropout":
                st.error(f"Status: {predicted_label[0]}")
            elif predicted_label[0] == "Enrolled":
                st.warning(f"Status: {predicted_label[0]}")
            else:
                st.success(f"Status: {predicted_label[0]}")
            
        except Exception as e:
            st.error(f"Terjadi kesalahan saat melakukan prediksi: {str(e)}")
    