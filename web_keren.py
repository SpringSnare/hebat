import streamlit as st
import requests
from streamlit_lottie import st_lottie

# 1. Konfigurasi Halaman Utama
st.set_page_config(page_title="Website Multipage Rhaka", page_icon="⭐", layout="centered")

# 2. Fungsi Pembaca Animasi Lottie (Aman dari eror)
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None
    return None

# Load beberapa animasi berbeda untuk tiap halaman
lottie_home = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_49rdyysj.json") # Roket
lottie_profile = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_q0uM3n.json") # Tepuk tangan

# 3. MEMBUAT MENU NAVIGASI (SIDEBAR)
st.sidebar.title("🧭 Navigasi Web")
st.sidebar.write("Pilih halaman yang ingin kamu buka:")
# Radio button untuk memilih halaman
halaman = st.sidebar.radio(
    "Pilih Menu:",
    ["🏠 Beranda", "👤 Profil Rhaka", "🎨 Galeri Warna-Warni"]
)

st.sidebar.divider()
st.sidebar.write("Dibuat dengan 💖 oleh Rhaka")

# 4. KONTEN MASING-MASING HALAMAN

# --- HALAMAN 1: BERANDA ---
if halaman == "🏠 Beranda":
    st.title("🚀 Selamat Datang di Beranda!")
    st.subheader("Halaman utama website keren buatan Rhaka")
    st.divider()
    
    if lottie_home:
        st_lottie(lottie_home, height=250, key="home_anim")
        
    st.write(
        "Ini adalah halaman utama website kamu. Kamu bisa menjelajahi halaman lainnya "
        "dengan mengklik menu di sebelah kiri (sidebar)!"
    )
    st.info("💡 **Tips:** Jika menu di sebelah kiri tidak muncul, klik tanda panah kecil **(>)** di pojok kiri atas browser kamu!")

# --- HALAMAN 2: PROFIL RHAKA ---
elif halaman == "👤 Profil Rhaka":
    st.title("👤 Profil Pembuat Website")
    st.subheader("Kenalan lebih dekat dengan sang Developer!")
    st.divider()
    
    if lottie_profile:
        st_lottie(lottie_profile, height=200, key="profile_anim")
        
    # Kamu bisa ganti tulisan di bawah ini dengan ceritamu sendiri!
    st.markdown("### 📝 Tentang Saya")
    st.write(
        "Halo semua! Nama saya **Rhaka**. Saya adalah seorang calon programmer hebat "
        "yang baru saja memulai perjalanan belajar coding Python."
    )
    st.write(
        "Website ini adalah karya pertama saya, dibuat dengan perjuangan menaklukkan "
        "berbagai macam eror sistem bersama AI pendamping saya! 💪"
    )
    
    st.success("🎯 **Hobi saya:** Belajar teknologi baru, mencoba hal baru, dan bermain game!")

# --- HALAMAN 3: GALERI WARNA ---
elif halaman == "🎨 Galeri Warna-Warni":
    st.title("🎨 Galeri Warna Custom")
    st.subheader("Eksperimen teks warna-warni di Streamlit")
    st.divider()
    
    st.write("Di halaman ini, kita bisa mewarnai teks sesuka hati menggunakan kode warna bawaan:")
    
    st.write("✨ :red[Teks Merah Menyala]")
    st.write("✨ :blue[Teks Biru Keren]")
    st.write("✨ :green[Teks Hijau Sukses]")
    st.write("✨ :orange[Teks Oranye Semangat]")
    st.write("✨ :violet[Teks Ungu Estetik]")
    
    st.divider()
    st.write("Kamu juga bisa menambahkan tulisan berwarna lain dengan format `:warna[tulisanmu]`!")