import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
all_data = pd.read_csv(r"https://raw.githubusercontent.com/faishalamin123/ecommerce_data/main/data/all_data.csv")
category_sales = pd.read_csv(r"https://raw.githubusercontent.com/faishalamin123/ecommerce_data/main/data/category_sales.csv")
monthly_sales = pd.read_csv(r"https://raw.githubusercontent.com/faishalamin123/ecommerce_data/main/data/monthly_sales.csv")


# Set page title
st.title("Dashboard Analisis Data : E-Commerce")

# Create tabs
tabs = ["Performa Penjualan", "Kategori Produk", "Distribusi Geografis", "Profiling Customers"]
selected_tab = st.sidebar.selectbox("Pilih Tab:", tabs)

if selected_tab == "Performa Penjualan":
    # Pertanyaan 1: Performa penjualan tiap bulan
    st.header("Performa penjualan tiap bulan")
    # Tambahkan widget untuk menentukan rentang waktu
    start_date = st.date_input("Pilih Tanggal Awal", pd.to_datetime(monthly_sales['month']).min())
    end_date = st.date_input("Pilih Tanggal Akhir", pd.to_datetime(monthly_sales['month']).max())

    # Convert the 'month' column to datetime.date
    monthly_sales['month'] = pd.to_datetime(monthly_sales['month']).dt.date

    # Filter data berdasarkan rentang waktu yang dipilih
    filtered_monthly_sales = monthly_sales[(monthly_sales['month'] >= start_date) & (monthly_sales['month'] <= end_date)]

    # Visualisasi baru berdasarkan rentang waktu yang dipilih
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8), sharex=True)

    # Plot Sales Volume
    axes[0].plot(
        filtered_monthly_sales['month'],
        filtered_monthly_sales['sales_volume'],
        marker='o',
        linewidth=2,
        color='turquoise'
    )
    axes[0].set_ylabel('Sales Volume')
    axes[0].set_title('Monthly Sales Volume')

    # Plot Sales Value
    axes[1].plot(
        filtered_monthly_sales['month'],
        filtered_monthly_sales['sales_value'],
        marker='o',
        linewidth=2,
        color='#15B01A'
    )
    axes[1].set_ylabel('Sales Value')
    axes[1].set_xlabel('Month')
    axes[1].set_title('Monthly Sales Value')

    # Menampilkan plot
    st.pyplot(fig)
    
    # Expander untuk penjelasan performa penjualan
    with st.expander("Analisis Performa Penjualan"):
        st.markdown("""
        Merujuk pada hasil line chart baik dalam sales volume dan sales value menunjukkan performa penjualan e-commerce 
        sejak tahun 2017 hingga tahun 2016-09 hingga 2018-08 berada pada tren positif. Akan tetapi, dalam tiga bulan terakhir, 
        nilai dari sales value menunjukkan adanya penurunan yang cukup signifikan dibandingkan bulan-bulan sebelumnya.
    """)

elif selected_tab == "Kategori Produk":
    # Pertanyaan 2: Kategori produk dengan volume penjualan tertinggi dan terendah
    st.header("Kategori produk dengan volume penjualan tertinggi dan terendah")
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

    colors = ["skyblue", "skyblue", "lightgray", "lightgray", "lightgray"]

    sns.barplot(x="sales_volume", y="product_category_name", data=category_sales.head(5), palette=colors,
                edgecolor="black", ax=ax[0])
    ax[0].set_ylabel(None)
    ax[0].set_xlabel(None)
    ax[0].set_title("Best Performing Product", loc="center", fontsize=18)
    ax[0].tick_params(axis='y', labelsize=15)

    sns.barplot(x="sales_volume", y="product_category_name",
                data=category_sales.sort_values(by="sales_volume", ascending=True).head(5),
                palette=colors, edgecolor="black", ax=ax[1])
    ax[1].set_ylabel(None)
    ax[1].set_xlabel(None)
    ax[1].invert_xaxis()
    ax[1].yaxis.set_label_position("right")
    ax[1].yaxis.tick_right()
    ax[1].set_title("Worst Performing Product", loc="center", fontsize=18)
    ax[1].tick_params(axis='y', labelsize=15)

    # Show plots
    st.pyplot(fig)
    
    # Expander untuk penjelasan performa penjualan produk
    with st.expander("Analisis Performa Penjualan Produk"):
        st.markdown("""
        Kategori produk dengan performa penjualan paling tinggi antara lain bed_bath_table, health_beauty, sports_leisure, computers_accessories, furniture_decor. Sedangkan kategori dengan volume penjualan terendah meliputi security_and_services, fashion_childrens_clothes, cds_dvds_musicals, la_cuisine, arts_and_craftmanship.
    """)

elif selected_tab == "Distribusi Geografis":
    # Pertanyaan 4: Distribusi geografis pelanggan
    st.header("Distribusi Geografis Pelanggan")

    # Visualisasi 1: Menampilkan kota dengan customer terbanyak
    st.subheader("Distribusi Customer berdasarkan Kota")
    city_counts = all_data['customer_city'].value_counts()
    top_cities = city_counts.head(10)

    st.set_option('deprecation.showPyplotGlobalUse', False)

    plt.figure(figsize=(12, 6))
    top_cities.plot(kind='bar', color='skyblue', edgecolor="black")
    plt.title('Top 10 Cities by Number of Customers')
    plt.xlabel('City')
    plt.ylabel('Number of Customers')
    plt.xticks(rotation=45, ha='right')
    st.pyplot()

    # Visualisasi 2: Menampilkan negara bagian dengan jumlah customer terbanyak
    st.subheader("Distribusi Customer berdasarkan Negara Bagian")
    states_counts = all_data['customer_state'].value_counts()
    top_states = states_counts.head(10)

    plt.figure(figsize=(12, 6))
    top_states.plot(kind='bar', color='skyblue', edgecolor="black")
    plt.title('Top 10 States by Number of Customers')
    plt.xlabel('States')
    plt.ylabel('Number of Customers')
    plt.xticks(rotation=45, ha='right')
    st.pyplot()

    # Expander untuk penjelasan distribusi pelanggan
    with st.expander("Analisis distribusi pelanggan"):
        st.markdown("""
        Penduduk Brasil memiliki kecenderungan terkonsentrasi di wilayah pesisir timur Brazil. Sebagian besar kota-kota besar dan pusat kegiatan ekonomi dan budaya Brasil terletak di sepanjang pesisir timur, terutama di wilayah pesisir Atlantik. Wilayah ini termasuk kota-kota seperti Rio de Janeiro, São Paulo, Salvador, dan Minas Gerais. Sehingga dilihat dari distribusi persebaran pelanggan memang paling banyak terkonsentrasi pada tiga negara Rio de Janeiro, São Paulo, dan Minas Gerais.
    """)

elif selected_tab == "Profiling Customers":
    # Pertanyaan 3: Profil karakteristik pelanggan
    st.header("Analisis Lanjutan Profiling Customers Menggunakan RFM")
    with st.expander("Metode yang digunakan"):
        st.markdown("""
        - Customer Profiling adalah suatu proses pengelompokan pelanggan berdasarkan kesamaan karakteristik yang dimilikinya [1].
        - Model RFM merupakan metode clustering yang didasarkan pada tiga variabel yaitu Recency, Frequency, Monetary (RFM). Variabel-variabel tersebut meliputi Recency (rentang terakhir kali transaksi dilakukan), Frequency (jumlah transaksi dalam satu periode), dan Monetary (nilai uang yang dikeluarkan pelanggan selama transaksi). Semakin kecil rentang Recency, semakin banyak Frequency, dan semakin besar Monetary, maka skor R, F, dan M juga semakin besar [1].
    """)
    
    st.subheader("Distribusi Nilai Recency, Frequency, dan Monetary")
    # Convert 'order_purchase_timestamp' to datetime if it's not already
    all_data['order_purchase_timestamp'] = pd.to_datetime(all_data['order_purchase_timestamp'], errors='coerce')

    # Handle any remaining missing or NaN values after conversion
    all_data = all_data.dropna(subset=['order_purchase_timestamp'])

    current_date = all_data['order_purchase_timestamp'].max()
    rfm_data = all_data.groupby('customer_id').agg({
        'order_purchase_timestamp': lambda x: (current_date - x.max()).days,
        'order_id': 'count',
        'price': 'sum'
    }).reset_index()

    rfm_data.columns = ['customer_id', 'recency', 'frequency', 'monetary']

    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    sns.histplot(rfm_data['recency'], bins=20, kde=True, color='skyblue')
    plt.title('Recency Distribution')

    plt.subplot(1, 3, 2)
    sns.histplot(rfm_data['frequency'], bins=20, kde=True, color='salmon')
    plt.title('Frequency Distribution')

    plt.subplot(1, 3, 3)
    sns.histplot(rfm_data['monetary'], bins=20, kde=True, color='green')
    plt.title('Monetary Distribution')

    plt.tight_layout()

    # Show plots for RFM analysis
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Show plots for RFM analysis
    st.pyplot()

    # Mengurutkan customer berdasarkan recency, frequency, & monetary score
    rfm_data['r_rank'] = rfm_data['recency'].rank(ascending=False)
    rfm_data['f_rank'] = rfm_data['frequency'].rank(ascending=True)
    rfm_data['m_rank'] = rfm_data['monetary'].rank(ascending=True)

    # Menormalisasi ranking customers
    rfm_data['r_rank_norm'] = (rfm_data['r_rank'] / rfm_data['r_rank'].max()) * 100
    rfm_data['f_rank_norm'] = (rfm_data['f_rank'] / rfm_data['f_rank'].max()) * 100
    rfm_data['m_rank_norm'] = (rfm_data['m_rank'] / rfm_data['m_rank'].max()) * 100

    rfm_data.drop(columns=['r_rank', 'f_rank', 'm_rank'], inplace=True)

    # Menentukan skor rfm customer
    rfm_data['RFM_score'] = 0.15 * rfm_data['r_rank_norm'] + 0.28 * rfm_data['f_rank_norm'] + 0.57 * rfm_data[
        'm_rank_norm']
    rfm_data['RFM_score'] *= 0.05
    rfm_data = rfm_data.round(2)
    rfm_data[['customer_id', 'RFM_score']].head(7)

    # Segmentasi customer berdasarkan RFM_score
    rfm_data["customer_segment"] = np.where(
        rfm_data['RFM_score'] > 4.5, "Top customers", (np.where(
            rfm_data['RFM_score'] > 4, "High-value customer", (np.where(
                rfm_data['RFM_score'] > 3, "Medium-value customer", np.where(
                    rfm_data['RFM_score'] > 1.6, 'Low-value customers', 'Lost customers'))))))

    rfm_data[['customer_id', 'RFM_score', 'customer_segment']].head(10)
    
    # Show RFM analysis results as a bar chart with specified colors and custom order
    st.subheader("Segmentasi Pelanggan Berdasarkan RFM Score")
    st.write("Berikut adalah hasil segmentasi pelanggan berdasarkan RFM Score:")

    # Determine the top two customer segments
    top_segments = rfm_data['customer_segment'].value_counts().nlargest(2).index.tolist()

    # Set colors for each segment
    colors_ = ['lightgray', 'lightgray', 'skyblue', 'skyblue', 'lightgray']

    # Define custom order for x-axis
    custom_order = ['Top customers', 'High-value customer', 'Medium-value customer', 'Low-value customers', 'Lost customers']

    # Plot bar chart for customer segments with custom order
    plt.figure(figsize=(10, 6))
    sns.countplot(x='customer_segment', data=rfm_data, order=custom_order, palette=colors_, edgecolor='black')
    plt.title('Jumlah Pelanggan berdasarkan Segment')
    plt.xlabel('Segment Pelanggan')
    plt.ylabel('Jumlah Pelanggan')
    plt.xticks(rotation=45, ha='right')
    st.pyplot()
    
    # Expander untuk penjelasan profil pelanggan
    with st.expander("Hasil Analisis RFM"):
        st.markdown("""
        - Distribusi recency yang condong ke kiri menunjukkan kondisi sebagian besar customer baru-baru ini melakukan transaksi.
        - Distribusi frequency dengan mean rendah dan skewness yang tinggi menunjukkan kondisi sebagian besar pelanggan hanya melakukan sedikit transaksi.
        - Distribusi monetary menunjukkan bahwa sebagian besar transaksi memiliki nilai yang relatif rendah. Kondisi ini terjadi karena sebagian besar transaksi memiliki harga yang lebih rendah daripada harga rata-rata, dan terdapat sejumlah transaksi dengan nilai yang signifikan di atas rata-rata.
        - Jenis customers e-commerce paling banyak merupakan low dan medium value customers. Hal ini menunjukkan bahwa sebagian besar pelanggan cenderung memiliki nilai transaksi yang rendah atau memiliki kombinasi nilai dan frekuensi transaksi yang belum begitu tinggi.
    """)
    with st.expander("Hasil Analisis RFM"):
        st.markdown("""
        Perusahaan e-commerce dapat mempertimbangkan berbagai strategi untuk meningkatkan nilai dan frekuensi transaksi dari segmen pelanggan low dan medium value customers. Perusahaan dapat melakukan campaign dengan memberikan program insentif berupa cashback atau voucer, penawaran khusus, atau membuat media promosi yang dapat merangsang pelanggan untuk melakukan lebih banyak transaksi.
    """)
    
# Tambahkan di bagian paling bawah skrip
st.markdown("""
    ---  
    © 2023 Faishal Amin A.
""")
