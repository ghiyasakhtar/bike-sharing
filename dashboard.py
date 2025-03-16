import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick

per_hour = pd.read_csv("hour.csv")
hour_df = per_hour.copy()
day_df = pd.read_csv("day.csv")

def categorize_time(hour):
    if 6 <= hour <= 11:
        return "Pagi"
    elif 12 <= hour <= 17:
        return "Siang"
    elif 18 <= hour <= 23:
        return "Sore"
    else:
        return "Malam"

hour_df["time_category"] = hour_df["hr"].apply(categorize_time)

st.title("Bike Sharing Data Dashboard")
st.write("Dashboard ini menampilkan analisis data penggunaan Bike Sharing berdasarkan waktu, musim, dan kondisi cuaca.")
st.image("https://raw.githubusercontent.com/ghiyasakhtar/bike-sharing/refs/heads/main/dataset-cover.jpeg")

# --- Pertanyaan 1: Waktu Aktivitas Pengguna ---
st.header("1st Insights: Aktivitas Pengguna Berdasarkan Waktu")
peak_hours = per_hour.nlargest(5, "cnt").sort_values(by="hr")
off_peak_hours = per_hour.nsmallest(5, "cnt").sort_values(by="hr")

col1, col2 = st.columns(2)
with col1:
    st.markdown("<h2 style='font-size:15px; color:white;'>Jam dengan Penggunaan Tertinggi</h2>", unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(data=peak_hours, x='hr', y='cnt', palette='crest', ax=ax)
    ax.set_xticklabels([f"{h}:00" for h in peak_hours['hr']])
    ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{int(x/1000)}k'))
    ax.set_xlabel("Waktu (Jam)")
    ax.set_ylabel("Jumlah Pengguna")
    st.pyplot(fig)

with col2:
    st.markdown("<h2 style='font-size:15px; color:white;'>Jam dengan Penggunaan Terendah</h2>", unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(data=off_peak_hours, x='hr', y='cnt', palette='crest', ax=ax)
    ax.set_xticklabels([f"{h}:00" for h in off_peak_hours['hr']])
    ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{int(x/1000)}k'))
    ax.set_xlabel("Waktu (Jam)")
    ax.set_ylabel("Jumlah Pengguna")
    st.pyplot(fig)

# --- Pertanyaan 2: Dampak Musim dan Cuaca ---
st.header("2nd Insights: Pengaruh Musim dan Cuaca terhadap Penggunaan")
option = st.selectbox("Jumlah Pengguna berdasarkan:",
                      ["Musim dan Kondisi Cuaca",
                       "Musim",
                       "Kondisi Cuaca"])

if option == "Musim dan Kondisi Cuaca":
    all_df = day_df.groupby(by=['season', 'weathersit']).agg({'cnt': 'sum'}).reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=all_df, x='season', y='cnt', hue='weathersit', palette='crest', ax=ax)
    ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{int(x/1000)}k'))
    ax.set_xlabel('Musim')
    ax.set_ylabel('Jumlah Pengguna')
    ax.set_title('Jumlah Pengguna berdasarkan Musim dan Kondisi Cuaca')
    ax.legend(title='Kondisi Cuaca', bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(fig)

elif option == "Musim":
    seasonal_df = day_df.groupby(by='season').agg({'cnt': 'sum'}).reset_index()
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=seasonal_df, x='season', y='cnt', palette='coolwarm', ax=ax)
    ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{int(x/1000)}k'))
    ax.set_xlabel('Musim')
    ax.set_ylabel('Jumlah Pengguna')
    ax.set_title('Jumlah Pengguna berdasarkan Musim')
    st.pyplot(fig)

elif option == "Kondisi Cuaca":
    season_bound_df = day_df.groupby(by='weathersit').agg({'cnt': 'sum'}).reset_index()
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=season_bound_df, x='weathersit', y='cnt', palette='coolwarm', ax=ax)
    ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{int(x/1000)}k'))
    ax.set_xlabel('Kondisi Cuaca')
    ax.set_ylabel('Jumlah Pengguna')
    ax.set_title('Jumlah Pengguna berdasarkan Kondisi Cuaca')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=15)
    st.pyplot(fig)

# --- Analisis Lanjutan: Clustering Waktu ---
st.header("Analisis Lanjutan")
st.subheader("Jumlah Pengguna berdasarkan Waktu Penggunaan")
clustering_result = hour_df.groupby("time_category")["cnt"].sum().reset_index()

fig, ax = plt.subplots(figsize=(7, 4))
sns.barplot(x="time_category", y="cnt", data=clustering_result, palette="crest", ax=ax)
ax.set_xlabel("Kategori Waktu")
ax.set_ylabel("Jumlah Pengguna")
ax.set_title("Total Pengguna Berdasarkan Waktu Penggunaan")
ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{int(x/1000)}k'))
st.pyplot(fig)

# --- Filter Data Berdasarkan Waktu ---
with st.sidebar:
    st.subheader("🔍See More Details Here")
    st.write("Eksplorasi Data Berdasarkan Jam")
    selected_hour = st.slider("Pilih Jam (0-23):", min_value=0, max_value=23, value=12)
    filtered_data = per_hour[per_hour["hr"] == selected_hour]

    if not filtered_data.empty:
        st.write(f"Data untuk jam {selected_hour}:00")
        st.dataframe(filtered_data)
    else:
        st.write("Tidak ada data untuk jam ini.")

st.write("© 2025 - Ghiyas Akhtar Razi Ramadhan")
