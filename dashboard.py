import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

season_labels = {1: "Semi", 2: "Panas", 3: "Gugur", 4: "Dingin"}
weather_labels = {
    1: "Cerah, Sedikit berawan",
    2: "Berkabut, mendung, berawan sebagian",
    3: "Hujan ringan, salju ringan, badai petir ringan",
}

st.set_page_config(page_title="Dashboard Analisis Data", layout="wide")
st.title("Dashboard Dicoding Project 'Bike Sharing' 📊 ")

tab1, tab2 = st.tabs(["Visualisasi Data", "Analisis RFM"])

with tab1:
    st.subheader("Visualisasi Data")
    season_filter = st.selectbox("Pilih Musim:", ["Semua"] + list(season_labels.values()))

    if season_filter != "Semua":
        selected_season = list(season_labels.keys())[list(season_labels.values()).index(season_filter)]
        filtered_df = hour_df[hour_df['season'] == selected_season]
    else:
        filtered_df = hour_df

    per_hour = filtered_df.groupby('hr').agg({'cnt': 'sum'}).reset_index()
    peak_hours = per_hour.nlargest(5, 'cnt').sort_values(by='hr')
    off_peak_hours = per_hour.nsmallest(5, 'cnt').sort_values(by='hr')

    fig1, ax1 = plt.subplots(figsize=(6, 3))
    sns.barplot(data=peak_hours, x='hr', y='cnt', palette='crest', ax=ax1)
    ax1.set_title("Jam dengan Penggunaan Tertinggi")
    ax1.set_xlabel("Waktu (Jam)")
    ax1.set_ylabel("Jumlah Pengguna")
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots(figsize=(6, 3))
    sns.barplot(data=off_peak_hours, x='hr', y='cnt', palette='crest', ax=ax2)
    ax2.set_title("Jam dengan Penggunaan Terendah")
    ax2.set_xlabel("Waktu (Jam)")
    ax2.set_ylabel("Jumlah Pengguna")
    st.pyplot(fig2)

    day_df['season'] = day_df['season'].map(season_labels)
    day_df['weathersit'] = day_df['weathersit'].map(weather_labels)

    fig3 = px.bar(day_df, x='season', y='cnt', color='weathersit',
                  title='Jumlah Pengguna berdasarkan Musim dan Kondisi Cuaca', width=600, height=350)
    st.plotly_chart(fig3)

with tab2:
    st.subheader("Analisis RFM")

    rfm_data = pd.DataFrame({
        'Recency': np.random.randint(1, 100, 500),
        'Frequency': np.random.randint(1, 50, 500),
        'Monetary': np.random.randint(1000, 50000, 500)
    })

    fig4, ax4 = plt.subplots(figsize=(6, 3))
    sns.histplot(rfm_data['Recency'], bins=30, kde=True, ax=ax4)
    ax4.set_title("Recency Distribution")
    st.pyplot(fig4)

    fig5, ax5 = plt.subplots(figsize=(6, 3))
    sns.histplot(rfm_data['Monetary'], bins=30, kde=True, ax=ax5)
    ax5.set_title("Monetary Distribution")
    st.pyplot(fig5)

    rfm_data['R_Score'] = pd.qcut(rfm_data['Recency'], q=4, labels=[4, 3, 2, 1])
    rfm_data['M_Score'] = pd.qcut(rfm_data['Monetary'], q=4, labels=[1, 2, 3, 4])
    rfm_pivot = rfm_data.pivot_table(index='R_Score', columns='M_Score', values='Recency', aggfunc='count')

    fig6, ax6 = plt.subplots(figsize=(6, 4))
    sns.heatmap(rfm_pivot, annot=True, fmt=".0f", cmap="Blues", linewidths=0.5, ax=ax6)
    ax6.set_title("Heatmap Skor RFM")
    ax6.set_xlabel("Skor Monetary")
    ax6.set_ylabel("Skor Recency")
    st.pyplot(fig6)

st.write("© 2025 - Ghiyas Akhtar Razi Ramadhan")
