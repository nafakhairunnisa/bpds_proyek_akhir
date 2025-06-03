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

Sumber data: [Student Data](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

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

Business dashboard adalah alat visualisasi yang menyajikan data analitik secara interaktif untuk mendukung pengambilan keputusan. Pada studi kasus ini, dashboard digunakan untuk mengetahui alasan tingginya dropout berdasarkan fitur-fitur yang memiliki keterkaitan signifikan dengan status mahasiswa. Dengan demikian, pihak institut dapat mengidentifikasi penyebab utama mahasiswa dropout dan mengambil keputusan berbasis data.

Berikut komponen yang tercantum dalam dashboard ditunjukkan pada tabel 1.

Tabel 1. Komponen Dashboard
| Komponen | Visualisasi | Jenis Data | Tujuan |
| ----------------------------- | --------------------------- | ------------- | ------------- |
| **KPI Summary** | Total Mahasiswa | Ringkasan | Menyajikan ringkasan data mahasiswa |
| **Filter** | Course | Filter Global | Filter berdasarkan program studi |
| Status | Donut Chart | Label | Mengetahui jumlah tiap status mahasiswa (Enrolled, Graduated, Dropout) |
| Curricular units 1st Semester grade  | Boxplot | Numerikal | Melihat distribusi nilai IP di semester 1 dan hubungannya dengan status mahasiswa |
| Curricular units 2nd Semester grade | Boxplot | Numerikal | Melihat distribusi nilai IP di semester 2 dan hubungannya dengan status mahasiswa |
| Average Grade | Boxplot | Numerikal | Melihat IPK |
| Curricular units 2nd Semester enrolled | Horizontal Bar Chart | Numerikal | Banyaknya SKS yang didaftarkan oleh mahasiswa |
| Application_mode | Treemap | Kategorikal | Jalur masuk mana yang sering menghasilkan mahasiswa dropout |
| Financial & Support Factors | Stacked Bar Chart | Kategorikal | Melihat gap dalam UKT terbaru, debtor, beasiswa |

Tools yang digunakan untuk membuat dashboard adalah Tableau Public versi 2024.1. Dashboard ini dibuat interaktif agar siapapun dapat mengeksplorasi dan memperoleh insight secara mandiri dari data yang tersedia.

**Preview Dashboard**
![HR Dashboard](nafa-khairunnisa-dashboard.png)
Gambar 1. Cuplikan Dashboard

Tautan dashboard dapat diakses [di sini](https://public.tableau.com/shared/4QBMDBW99?:display_count=n&:origin=viz_share_link).

## Menjalankan Sistem Machine Learning

Model machine learning yang telah dibuat dideploy ke dalam sebuah aplikasi streamlit. Model yang digunakan yaitu Random Forest yang merupakan model terbaik dengan akurasi 74% dan Random Forest unggul dalam menghasilkan nilai f1-score yang stabil.

Berikut cara menjalankan sistem machine learning:

**1. Buka direktori file app.py berada melalui anaconda**

```
cd ...\bpds_proyek-akhir
```

**2. Run streamlit app**

```
streamlit run app.py
```

Anda juga dapat mengakses aplikasi streamlitnya melalui link berikut: [Link Streamlit](https://status-mahasiswa-predict.streamlit.app/).

## Conclusion

Berdasarkan hasil analisis data, visualisasi dashboard, serta implementasi model machine learning, proyek ini berhasil mengidentifikasi faktor-faktor utama yang memengaruhi banyaknya mahasiswa yang dropout.

**Insights:**

### 1. Karakteristik Dataset dan Demografis
Dataset mencakup total 4.424 mahasiswa. Sebagian besar mahasiswa berusia antara 15–25 tahun, belum menikah, dan mengikuti kelas siang (89.08%). Hanya sebagian kecil yang mengikuti kelas malam (10.92%). Status pernikahan mayoritas adalah single, dengan jumlah yang sangat kecil berasal dari kelompok menikah, bercerai, atau duda/janda. Mahasiswa penerima beasiswa hanya mencakup 24.84%, sedangkan 11.37% mahasiswa tercatat sebagai debitur. Sementara itu, 11.93% mahasiswa belum memperbarui informasi pembayaran SPP mereka.

### 2. Analisis Status dan Course
Sebagian besar mahasiswa telah lulus (49.93%), diikuti oleh yang dropout (32.12%) dan mahasiswa aktif/enrolled (17.95%). Tingginya angka dropout menjadi indikator penting untuk evaluasi sistem pembelajaran atau faktor eksternal lainnya. Course dengan jumlah mahasiswa terbanyak adalah Nursing dan Vet Nursing, disusul oleh bidang seperti Journalism, Social Service, dan Management. Dominasi bidang kesehatan menunjukkan minat tinggi terhadap jurusan tersebut dibandingkan jurusan lain seperti Agronomy atau Marketing.

### 3. Analisis Waktu Kuliah dan Status Pernikahan
Meskipun jumlah mahasiswa kelas siang jauh lebih banyak, kelas malam tampaknya memiliki tingkat kelulusan yang lebih tinggi dan tingkat dropout yang lebih rendah. Hal ini mengindikasikan bahwa mahasiswa malam mungkin lebih termotivasi atau memiliki komitmen belajar yang lebih tinggi. Dari sisi status pernikahan, mahasiswa yang belum menikah memiliki tingkat kelulusan lebih tinggi dibandingkan yang sudah menikah. Mahasiswa yang bercerai atau duda/janda sangat sedikit dan tidak menunjukkan pola signifikan.

### 4. Analisis Akademik
Mahasiswa yang dropout memiliki rata-rata nilai dan jumlah mata kuliah yang dikreditkan lebih rendah dibandingkan mahasiswa yang lulus. Hal ini terlihat pada metrik seperti rata-rata nilai akhir (average grade), nilai semester 1 dan 2, serta jumlah mata kuliah yang disetujui di semester 2. Sebaliknya, mahasiswa yang lulus menunjukkan performa akademik yang lebih stabil sejak awal. Usia saat masuk kuliah tidak menunjukkan pengaruh signifikan terhadap kinerja akademik.

### 5. Faktor Signifikan yang Berpengaruh
Beberapa faktor terlihat konsisten memengaruhi status akhir mahasiswa:

**Faktor Demografis dan Administratif:**

- Waktu kuliah: Mahasiswa kelas malam menunjukkan performa lebih baik dibanding kelas siang.
- Status beasiswa: Mahasiswa penerima beasiswa cenderung memiliki performa lebih baik.
- Status utang dan pembayaran SPP: Mahasiswa tanpa utang dan yang memperbarui informasi SPP menunjukkan kecenderungan kelulusan lebih tinggi.

**Faktor Akademik:**

- Nilai semester 1 dan 2
- Rata-rata nilai keseluruhan (average grade)
- Jumlah dan kelulusan mata kuliah semester awal

**Faktor Course dan Latar Belakang:**

- Course Nursing dan Vet Nursing memiliki jumlah mahasiswa terbanyak dan kemungkinan kontribusi kelulusan tinggi.
- Course dengan dominasi dropout seperti Management perlu mendapatkan perhatian khusus terkait kurikulum atau dukungan akademik.

### Rekomendasi Action Items

Berdasarkan analisis yang telah dilakukan, berikut rekomendasi action items untuk mengurangi tingkat dropout mahasiswa:

1. **Program Bimbingan Akademik Intensif**
Banyak mahasiswa yang dropout menunjukkan performa akademik rendah sejak semester pertama. Oleh karena itu:

   - Menerapkan sistem monitoring akademik yang lebih ketat, terutama untuk mahasiswa dengan nilai rendah di semester 1 dan 2
   - Menyediakan program bimbingan belajar tambahan untuk mata kuliah dengan tingkat kelulusan rendah
   - Membuat program mentoring yang menghubungkan mahasiswa baru dengan senior yang berprestasi

2. **Penyesuaian Jadwal dan Sistem Pembelajaran**
Insight menunjukkan bahwa mahasiswa kelas siang memiliki tingkat dropout lebih tinggi dibanding kelas malam. Maka dari itu:

   - Mengoptimalkan jadwal kuliah siang dengan mempertimbangkan faktor-faktor yang mempengaruhi kehadiran
   - Menerapkan sistem pembelajaran hybrid (kombinasi online dan offline) untuk memberikan fleksibilitas
   - Menyediakan rekaman perkuliahan untuk mahasiswa yang tidak bisa hadir

3. **Program Dukungan Finansial dan Beasiswa**
Ditemukan bahwa sebagian besar mahasiswa memiliki utang, namun tetap membayar SPP tepat waktu, sementara jumlah penerima beasiswa masih rendah. Untuk itu:

   - Memperluas program beasiswa untuk mahasiswa berprestasi dengan latar belakang ekonomi rendah
   - Menyediakan program kerja paruh waktu di kampus untuk membantu mahasiswa dengan masalah finansial
   - Membuat sistem pembayaran SPP yang lebih fleksibel dengan skema cicilan yang terjangkau

4. **Peningkatan Kualitas Course Management**
Beberapa program studi seperti Management memiliki tingkat dropout tinggi. Maka:

   - Melakukan evaluasi dan perbaikan kurikulum untuk course dengan tingkat dropout tinggi
   - Meningkatkan kualitas pengajaran dengan program pengembangan dosen
   - Membuat program orientasi yang lebih komprehensif untuk mahasiswa baru, terutama untuk course dengan tingkat dropout tinggi