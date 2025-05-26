# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Namun, tingginya tingkat mahasiswa yang tidak menyelesaikan studinya (dropout) menjadi permasalahan serius yang dapat memengaruhi akreditasi dan reputasi institusi.

Jaya Jaya Institut ingin secara dini mendeteksi mahasiswa yang berisiko tinggi mengalami dropout agar dapat diberikan bimbingan atau intervensi yang sesuai.

Untuk mengatasi tantangan tersebut, institusi ingin mengembangkan sistem berbasis data guna mendeteksi mahasiswa berisiko tinggi melakukan dropout secara dini dan memberikan intervensi yang tepat waktu.

### Permasalahan Bisnis

Berdasarkan pemahaman bisnis yang telah dijelaskan, berikut adalah permasalahan utama yang dihadapi oleh institut:

- Tingginya tingkat dropout yang berdampak pada akreditasi dan reputasi institusi pendidikan.
- Tidak adanya sistem pemantauan atau early warning system berbasis data yang dapat mendeteksi risiko dropout secara proaktif.
- Tidak adanya strategi retensi mahasiswa yang terukur dan berbasis analisis.
- Kurang optimalnya alokasi sumber daya pengajaran serta potensi kerugian finansial bagi institusi maupun mahasiswa.

### Cakupan Proyek

Proyek ini bertujuan menjawab tantangan tingginya dropout dengan memanfaatkan data historis akademik mahasiswa untuk mengidentifikasi faktor-faktor kunci yang memengaruhi keputusan keluar dari studi.

Proyek ini menggunakan data historis akademik dan latar belakang mahasiswa, termasuk aspek demografis dan sosial ekonomi, untuk:

- Melakukan eksplorasi data (EDA) untuk menemukan distribusi dan pola-pola yang mencurigakan.
- Menganalisis keterkaitan antara faktor seperti pendidikan orang tua, biaya kuliah, nilai semester, dan status akademik terhadap risiko dropout.
- Membangun model klasifikasi berbasis machine learning untuk prediksi dropout secara individual.
- Mengembangkan dashboard interaktif sebagai alat bantu monitoring dan pengambilan keputusan oleh staf akademik.
- Menyusun rekomendasi kebijakan berbasis data untuk meningkatkan retensi mahasiswa.

### Persiapan

Sumber data: [Employee Data](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

**Setup Environment**

Untuk menjalankan analisis dan aplikasi prediksi, lingkungan Python perlu disiapkan dengan langkah berikut:

**1. Clone this repository to your local computer**

```
git@github.com:nafakhairunnisa/bpds_proyek-pertama.git
```

**2. Setup Environment**
**Pilihan 1: Menggunakan Anaconda**

```
conda create --name main-ds python=3.12.9
conda activate main-ds
pip install -r requirements.txt
pip install streamlit
```

**Pilihan 2: Menggunakan pipenv (Virtual Environment di Shell/Terminal)**

```
mkdir bpds_proyek-pertama
cd bpds_proyek-pertama
pipenv install --python 3.12.9
pipenv shell
pip install -r requirements.txt
pip install streamlit
```

## Business Dashboard

Business dashboard adalah alat visualisasi yang menyajikan data analitik secara interaktif untuk mendukung pengambilan keputusan. Pada studi kasus ini, dashboard digunakan untuk mengetahui pengaruh tingginya dropout berdasarkan fitur-fitur yang memiliki keterkaitan signifikan dengan status mahasiswa. Dengan demikian, pihak institut dapat mengidentifikasi penyebab utama mahasiswa dropout dan mengambil keputusan berbasis data.

Berikut komponen yang tercantum dalam dashboard ditunjukkan pada tabel 1.

Tabel 1. Komponen Dashboard
| Komponen | Visualisasi | Jenis Data | Tujuan |
| ----------------------------- | --------------------------- | ------------- | ------------- |
| **KPI Summary** | Total Mahasiswa | Ringkasan | Menyajikan ringkasan data mahasiswa |
| **Filter** | Course | Filter Global | Filter berdasarkan program studi |
| Status | Donut Chart | Label | Mengetahui jumlah tiap status mahasiswa (Enrolled, Graduated, Dropout) |
| Gender | Drill Down dari Donut Chart | Kategorikal | Melihat distribusi berdasarkan jenis kelamin |
| Curricular units 1st Semester grade  | Boxplot | Numerikal | Melihat distribusi nilai IP di semester 1 dan hubungannya dengan status mahasiswa |
| Curricular units 2nd Semester grade | Boxplot | Numerikal | Melihat distribusi nilai IP di semester 2 dan hubungannya dengan status mahasiswa |
| Average Grade | Boxplot | Numerikal | Melihat IPK |
| Curricular units 2nd Semester enrolled | Histogram | Numerikal | Apakah jarak rumah berpengaruh terhadap attrition |
| Application_mode | Treemap | Kategorikal | Jalur masuk mana yang sering menghasilkan mahasiswa dropout |
| Financial & Support Factors | Stacked Bar Chart | Kategorikal | Melihat gap dalam UKT terbaru, debtor, beasiswa |
| Side-by-side comparison (Graduate vs Dropout vs Enrolled) | Horizontal Bar Chart | Kategorikal | Perbandingan visual antar status mahasiswa berdasarkan faktor akademik dan non-akademik |

Tools yang digunakan untuk membuat dashboard adalah Tableau Public versi 2024.1. Dashboard ini dibuat interaktif agar siapapun dapat mengeksplorasi dan memperoleh insight secara mandiri dari data yang tersedia.

**Preview Dashboard**
![HR Dashboard](nafa-khairunnisa-dashboard.png)
Gambar 1. Cuplikan Dashboard

Tautan dashboard dapat diakses [di sini](link).

## Menjalankan Sistem Machine Learning

Model machine learning yang telah dibuat dideploy ke dalam sebuah aplikasi streamlit. Model yang digunakan yaitu XGBoost yang merupakan model terbaik dengan akurasi 73% dan XGBoost unggul dalam menghasilkan nilai f1-score yang stabil.

Berikut cara menjalankan sistem machine learning:

**1. Buka direktori file predict.py berada melalui anaconda**

```
cd ...\bpds_proyek-akhir
```

**2. Run streamlit app**

```
streamlit run predict.py
```

Anda juga dapat mengakses aplikasi streamlitnya melalui link berikut: (Link Streamlit)[].

## Conclusion

Berdasarkan hasil analisis data, visualisasi dashboard, serta implementasi model machine learning, proyek ini berhasil mengidentifikasi faktor-faktor utama yang memengaruhi banyaknya mahasiswa yang dropout.

**Insights:**

### 1. Karakteristik Dataset dan Demografis

Dari total 4424 mahasiswa, lebih dari 50% mengalami dropout. Mayoritas mahasiswa berasal dari lokal, berjenis kelamin laki-laki, dan belum menikah. Sebagian besar mahasiswa memilih untuk belajar di malam hari dan berasal dari latar belakang keluarga dengan pendidikan dan pekerjaan rendah. Meskipun sebagian besar mahasiswa memiliki utang, mereka tetap membayar SPP tepat waktu. Jumlah penerima beasiswa dan mahasiswa dengan kebutuhan khusus relatif sedikit.

### 2. Analisis Status dan Course

Persentase dropout merupakan yang tertinggi (hampir setengah dari total), diikuti oleh mahasiswa yang lulus dan yang masih aktif. Course Nursing mencatat tingkat kelulusan tertinggi, sementara course lain memiliki jumlah mahasiswa yang lebih sedikit (kurang dari 400). Course Management dan Management (evening attendance) memiliki tingkat dropout tertinggi, yang menandakan minat rendah pada course tersebut.

### 3. Analisis Waktu Kuliah dan Status Pernikahan

Kelas malam menunjukkan tingkat kelulusan yang lebih tinggi dibandingkan kelas siang yang memiliki tingkat dropout lebih tinggi, mengindikasikan bahwa jadwal kuliah siang bisa menjadi tantangan. Dari segi status pernikahan, mahasiswa single memiliki tingkat kelulusan lebih tinggi dibandingkan mahasiswa yang sudah menikah. Status pernikahan lain seperti divorced, widower, dan legally separated memiliki distribusi yang sangat sedikit. Hal ini menunjukkan bahwa tanggungan mahasiswa single lebih aman sehingga masih bisa melanjutkan kuliah.

### 4. Analisis Akademik

Semakin banyak mata kuliah yang diambil dan dikreditkan, semakin tinggi nilai akhir yang diperoleh mahasiswa. Namun, usia saat masuk kuliah tidak terlalu mempengaruhi performa akademik mahasiswa.

### 5. Faktor Signifikan yang Berpengaruh

Faktor-faktor berikut memiliki pengaruh signifikan terhadap distribusi status mahasiswa:

**Faktor Demografis dan Administratif:**

- Application mode: Mahasiswa di atas 23 tahun
- Gender: Laki-laki
- Status beasiswa: Penerima beasiswa
- Status pembayaran: Pembayaran tepat waktu
- Status utang: Memiliki utang

**Faktor Akademik:**

- Nilai semester 1
- Nilai semester 2
- Jumlah mata kuliah yang diambil semester 2
- Rata-rata nilai (avg_grade)
- Tingkat kelulusan semester 1 (approval_rate_1st)
- Tingkat kelulusan semester 2 (approval_rate_2nd)

**Faktor Course dan Latar Belakang:**

- Course: Informatika dan Keperawatan
- Kualifikasi orang tua: Tidak diketahui

### Rekomendasi Action Items

Berdasarkan analisis yang telah dilakukan, berikut rekomendasi action items untuk mengurangi tingkat dropout mahasiswa:

1. **Program Bimbingan Akademik Intensif**

   - Menerapkan sistem monitoring akademik yang lebih ketat, terutama untuk mahasiswa dengan nilai rendah di semester 1 dan 2
   - Menyediakan program bimbingan belajar tambahan untuk mata kuliah dengan tingkat kelulusan rendah
   - Membuat program mentoring yang menghubungkan mahasiswa baru dengan senior yang berprestasi

2. **Penyesuaian Jadwal dan Sistem Pembelajaran**

   - Mengoptimalkan jadwal kuliah siang dengan mempertimbangkan faktor-faktor yang mempengaruhi kehadiran
   - Menerapkan sistem pembelajaran hybrid (kombinasi online dan offline) untuk memberikan fleksibilitas
   - Menyediakan rekaman perkuliahan untuk mahasiswa yang tidak bisa hadir

3. **Program Dukungan Finansial dan Beasiswa**

   - Memperluas program beasiswa untuk mahasiswa berprestasi dengan latar belakang ekonomi rendah
   - Menyediakan program kerja paruh waktu di kampus untuk membantu mahasiswa dengan masalah finansial
   - Membuat sistem pembayaran SPP yang lebih fleksibel dengan skema cicilan yang terjangkau

4. **Peningkatan Kualitas Course Management**
   - Melakukan evaluasi dan perbaikan kurikulum untuk course dengan tingkat dropout tinggi
   - Meningkatkan kualitas pengajaran dengan program pengembangan dosen
   - Membuat program orientasi yang lebih komprehensif untuk mahasiswa baru, terutama untuk course dengan tingkat dropout tinggi
