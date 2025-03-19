# Proyek Analisis Data: Bike Sharing

Proyek ini merupakan eksplorasi analisis data yang berfokus pada pemahaman pola penggunaan layanan Bike Sharing. Analisis dilakukan menggunakan Python dalam Jupyter Notebook, mencakup proses pembersihan data, visualisasi, serta pengambilan insight dari data yang tersedia.

## Fitur Utama
- Eksplorasi Data (Exploratory Data Analysis / EDA)
- Pembersihan dan Transformasi Data
- Visualisasi Data menggunakan Seaborn & Matplotlib
- Statistik Deskriptif dan Insight Data

## Dataset
Dataset yang digunakan dalam proyek ini merupakan data layanan Bike Sharing.

## Ringkasan Insight
Beberapa insight yang berhasil diperoleh dari analisis ini antara lain:
- Pola penggunaan sepeda cenderung meningkat pada akhir pekan dan musim panas.
- Terdapat korelasi antara suhu udara dan jumlah peminjaman sepeda.
- Pengguna terbagi dalam dua kategori utama: casual (tidak berlangganan) dan registered (berlangganan), dengan perbedaan perilaku yang signifikan.

## Contoh Visualisasi
Visualisasi yang digunakan dalam notebook mencakup:
- Grafik distribusi jumlah peminjaman per jam/hari
- Heatmap korelasi antar variabel
- Boxplot penggunaan sepeda berdasarkan kategori pengguna

## Teknologi & Library yang Digunakan
- pandas
- numpy
- matplotlib
- seaborn
- streamlit (untuk dashboard interaktif)

## Cara Menjalankan Proyek

### **1️⃣ Setup Virtual Environment**
#### **Menggunakan Anaconda**
```bash
conda create --name bike-sharing-env python=3.9
conda activate bike-sharing-env
pip install -r requirements.txt
```

#### **Menggunakan Pipenv (Shell/Terminal)**
```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

### **2️⃣ Menjalankan Jupyter Notebook**
```bash
jupyter notebook notebook.ipynb
```
Atau gunakan Google Colab untuk menjalankan secara online.

### **3️⃣ Menjalankan Dashboard Interaktif**
```bash
streamlit run dashboard.py
```
Pastikan file `dashboard.py` berada dalam direktori proyek yang benar.


## Penulis
Ghiyas Akhtar Razi Ramadhan
