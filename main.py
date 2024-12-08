import streamlit as st
import pandas as pd
import numpy as np
import openpyxl as xl




st.title("Pumbukuan for Shopee and Tokopedia")
st.write("use this app to format the .xlsx file from Shopee or Tokopedia")
st.write("## 1.  Select the shop to upload")
choice = st.selectbox("Select the shop to upload", ["Shopee", "Tokopedia"])
st.write(f"## 2.  Upload the .xlsx file from {choice}")



uploaded_file = st.file_uploader(f"Upload the .xlsx file for {choice}", type=['xlsx'])
if uploaded_file is not None:
    # You can process the file here
    df = pd.read_excel(uploaded_file)
    st.write("File uploaded successfully!")
    if choice == "Shopee":
        # Tremove all columsn that are not in Status Pesanan, Waktu Pembayaran Dilakukan, Nama Produk, Jumlah, Total Harga Produk, Username (Pembeli), Nama Penerima
        df = df[['Status Pesanan', 'Waktu Pembayaran Dilakukan', 'Nama Produk', 'Jumlah', 'Total Harga Produk', 'Username (Pembeli)', 'Nama Penerima']]
        df['Waktu Pembayaran Dilakukan'] = df['Waktu Pembayaran Dilakukan'].str.replace(r'\s+.*$', '', regex=True)
        #remove status pesanana entrys containing "Batal"
        df = df[~df['Status Pesanan'].str.contains('Batal')]
        df['Jumlah'] = pd.to_numeric(df['Jumlah'])
        #convert Total Harga Produk to numeric by removing thousand separator dots and converting to numeric
        df['Total Harga Produk'] = df['Total Harga Produk'].str.replace('.', '', regex=False)
        df['Total Harga Produk'] = pd.to_numeric(df['Total Harga Produk'])
        #create some score cards for most sold item (nama produk) total revenue (total harga produk) and total qty sold (jumlah)


        pass
    elif choice == "Tokopedia":
        # remove head, remove row 0, row 1 , and row 2, then reset index of the rows to be row 3 in this case
        df = df.iloc[3:]
        df = df.reset_index(drop=True)
        #the row 0 is the header, so we need to set the first row as the header
        df.columns = df.iloc[0]
        df = df.iloc[1:]
        #now rremove all columns that are not, Tanggal Pembayaran, Status Terakhir,Nama Produk,Jumlah Produk Dibeli, Harga Awal (IDR),Nama Pembeli, Nama Penerima
        df = df[['Tanggal Pembayaran', 'Status Terakhir', 'Nama Produk', 'Jumlah Produk Dibeli', 'Harga Awal (IDR)', 'Nama Pembeli', 'Nama Penerima']]
        #regex format date to dd-mm-yyyy in column "Tanggal Pembayaran" current date format is 16-11-2024 06:43:23 so a simply regex replace everything after the first white space
        df['Tanggal Pembayaran'] = df['Tanggal Pembayaran'].str.replace(r'\s+.*$', '', regex=True)
        # Convert columns to numeric types
        df['Jumlah Produk Dibeli'] = pd.to_numeric(df['Jumlah Produk Dibeli'])
        df['Harga Awal (IDR)'] = pd.to_numeric(df['Harga Awal (IDR)'])
        # Calculate total revenue
        df['Total Revenue'] = df['Jumlah Produk Dibeli'] * df['Harga Awal (IDR)']





        pass
    st.dataframe(df)
    if choice == "Shopee":
        metrics_container = st.container()
        col1, col2, col3 = metrics_container.columns(3)
        with col1:
            st.metric("Most Sold Item", df['Nama Produk'].value_counts().idxmax())
        with col2:
            st.metric("Total Revenue", df['Total Harga Produk'].sum())
        with col3:
            st.metric("Total Qty Sold", df['Jumlah'].sum())
    elif choice == "Tokopedia":
        metrics_container = st.container()
        col1, col2, col3 = metrics_container.columns(3)
        with col1:
            st.metric("Most Sold Item", df['Nama Produk'].value_counts().idxmax())
        with col2:
            st.metric("Total Revenue", df['Total Revenue'].sum())
        with col3:
            st.metric("Total Qty Sold", df['Jumlah Produk Dibeli'].sum())
    st.write("## 3.  Copy to clipboard")
    st.button("copy to clipboard")
    #copy the df to clipboard
    df.to_clipboard(index=False)
    

    



