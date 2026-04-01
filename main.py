import streamlit as st

# Pengaturan halaman (biar keren)
st.set_page_config(page_title="Fidz Store", page_icon="💰")

# Tampilan Utama
st.title("💰 Fidz Store")
st.subheader("JUBEL HASIL RESS")
st.write("---")

# Form Input untuk kamu/buyer
with st.form("input_form"):
    st.write("### Form Transaksi")
    nama_produk = st.text_input("Nama Akun/Produk")
    harga = st.number_input("Harga Jual (Rp)", min_value=0, step=5000)
    status = st.selectbox("Status Akun", ["Ready", "Sold", "Booked"])
    
    submitted = st.form_submit_button("Update Web")
    
    if submitted:
        st.success(f"Berhasil Update: {nama_produk} seharga Rp{harga:,}")

# List Produk (Contoh tampilan)
st.write("---")
st.write("### 📦 Stock Tersedia")
col1, col2 = st.columns(2)

with col1:
    st.info("**Akun FF Diamond**\n\nPrice: Rp50k\n\nStatus: READY")

with col2:
    st.info("**Akun Roblox Aetheria**\n\nPrice: Rp100k\n\nStatus: READY")
