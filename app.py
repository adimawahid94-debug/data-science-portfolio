import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Judul Utama & Profil Singkat
st.title("👨‍💻 Data Science Portfolio Dashboard")
st.subheader("Adhima Wahid Nugroho")
st.write("""
Seorang Data Science & Analyst enthusiast dengan latar belakang kemampuan analisis yang kuat. 
Berpengalaman dalam mengolah data mentah menjadi visualisasi interaktif dan model prediktif 
yang berorientasi pada solusi bisnis.
""")

st.markdown("---")

# 2. Dropdown Menu untuk Memilih Proyek (Sekarang ada 3 Proyek!)
project_choice = st.selectbox(
    "Silakan Pilih Proyek untuk Melihat Detail Analisis:",
    [
        "Analisis Perilaku Tipping Restoran", 
        "Prediksi Hotel Booking Demand & Revenue Loss",
        "Real-Time Fraud Detection & Monitoring"
    ]
)

# 3. Konten Berdasarkan Proyek yang Dipilih
if project_choice == "Analisis Perilaku Tipping Restoran":
    st.header("🍽️ Restaurant Tipping Behavior Analysis")
    st.write("**Deskripsi:** Proyek ini membedah faktor-faktor yang memengaruhi besaran tip pelanggan menggunakan Exploratory Data Analysis (EDA) dan Linear Regression untuk membantu manajemen meningkatkan kualitas layanan dan pendapatan pramusaji.")
    
    # PERBAIKAN METRIK: Menampilkan Angka Statistik Utama
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Total Data Sampel", value="244 Transaksi")
    col2.metric(label="Rata-rata Tagihan", value="$19.78")
    col3.metric(label="Faktor Utama", value="Total Bill")
    
    st.markdown("### 📊 Key Business Insights:")
    st.write("""
    * **Korelasi Kuat:** Besaran tip memiliki hubungan linear positif yang kuat dengan total tagihan (*total bill*). Semakin besar transaksi makan, semakin besar tip yang cenderung diberikan.
    * **Waktu Makan:** Makan malam (*Dinner*) menghasilkan rata-rata tip yang lebih tinggi dibandingkan makan siang (*Lunch*).
    * **Hari Potensial:** Hari Sabtu dan Minggu adalah hari di mana pelanggan paling royal dalam memberikan tip, menjadikannya waktu optimal untuk alokasi staf terbaik.
    """)

elif project_choice == "Prediksi Hotel Booking Demand & Revenue Loss":
    st.header("🏨 Hotel Booking Demand & Revenue Risk Analysis")
    st.write("**Deskripsi:** Menggunakan algoritma Machine Learning (XGBoost/Random Forest) untuk memprediksi risiko pembatalan (*cancellation*) pesanan hotel. Proyek ini bertujuan membantu manajemen hotel melakukan strategi overbooking yang aman dan meminimalkan potensi kehilangan pendapatan.")
    
    # Metrik Angka Proyek Hotel Berdasarkan Dampak Bisnis
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Akurasi Model", value="89%")
    col2.metric(label="Potensi Revenue Diselamatkan", value="~28%")
    col3.metric(label="Reduksi Pembatalan", value="15%")
    
    st.markdown("### 📊 Key Business Insights & Rekomendasi:")
    st.write("""
    * **Pola Pembatalan:** Pelanggan dengan *lead time* (jarak waktu booking ke waktu menginap) yang terlalu panjang memiliki probabilitas pembatalan yang jauh lebih tinggi.
    * **Jenis Deposit:** Pesanan tanpa deposit (*No Deposit*) menyumbang angka pembatalan terbesar dibandingkan dengan tipe *Non-Refundable*.
    * **Rekomendasi Bisnis:** Menerapkan kebijakan uang muka (DP) atau pengetatan aturan pembatalan gratis pada kamar-kamar yang dipesan jauh-jauh hari guna mengamankan pendapatan hotel.
    """)

elif project_choice == "Real-Time Fraud Detection & Monitoring":
    st.header("🛡️ Real-Time Fraud Detection & Monitoring")
    st.write("**Deskripsi:** Pengembangan sistem monitoring dan deteksi dini transaksi mencurigakan untuk meminimalkan kerugian finansial akibat tindakan fraud pada jaringan transaksi.")
    
    # Metrik Angka Proyek Fraud (Sesuai Data PDF Halaman 23 & 25)
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Kasus Fraud Tertangkap (Recall)", value="84%", delta="82 dari 98 kasus")
    col2.metric(label="Akurasi Deteksi (Precision)", value="93%")
    col3.metric(label="Efisiensi Biaya Investigasi", value="~24%", delta="Threshold 0.9")
    
    st.markdown("### 📊 Key Business Insights & Sistem Monitoring:")
    st.write("""
    * **Indikator Utama Fraud:** Transaksi dengan lonjakan nominal yang tidak biasa dalam waktu singkat (*velocity attack*) menjadi pola utama yang berhasil diidentifikasi oleh model.
    * **Skalabilitas Sistem:** Sistem ini mampu memetakan skor risiko (*risk score*) pada setiap transaksi masuk secara instan untuk memberikan keputusan *Approve* atau *Decline*.
    * **Dampak Bisnis:** Mengurangi waktu investigasi manual oleh tim analis fraud dan berhasil menyelamatkan potensi kerugian finansial perusahaan.
    """)

st.markdown("---")

# 4. Bagian Kontak
st.subheader("📬 Mari Berkolaborasi")
col_mail, col_link = st.columns(2)
col_mail.write("📧 **Email:** adimawahid94@gmail.com")
col_link.write("🔗 **LinkedIn:** [Profil LinkedIn Anda](https://www.linkedin.com/in/adhima-wahid-nugroho-424799118)")
