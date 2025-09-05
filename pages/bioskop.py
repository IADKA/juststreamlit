
# pages/2_Video.py
import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Video Rahasia Saya",
    page_icon="🎬",
    layout="centered"
)

# --- Judul dan Deskripsi ---
st.title("🎬 Sebuah kado kecil")
st.write("Selamat datang kak! Apakah kakak mau popcornnya sekalian?")
st.markdown("---")

# --- URL Video YouTube Unlisted Anda ---
# GANTI DENGAN URL VIDEO UNLISTED YOUTUBE ANDA YANG SEBENARNYA
youtube_unlisted_url = "https://www.youtube.com/watch?v=WE0Bqoa7Wsc&ab_channel=AndreKrismantara"

# Pastikan URLnya benar dan video sudah diatur sebagai 'Unlisted' di YouTube.
# Contoh URL yang valid: "https://www.youtube.com/watch?v=dQw4w9WgXcQ" (ini video publik, tapi sebagai contoh format)
# ATAU jika ingin video auto-play dan tanpa kontrol:
# youtube_unlisted_url = "https://www.youtube.com/embed/YOUR_UNLISTED_VIDEO_ID?autoplay=1&controls=0"


# --- Menampilkan Video ---
if youtube_unlisted_url == "https://www.youtube.com/watch?v=YOUR_UNLISTED_VIDEO_ID":
    st.error("⚠️ **Peringatan:** Harap ganti `YOUR_UNLISTED_VIDEO_ID` dengan URL video YouTube *unlisted* Anda yang sebenarnya!")
    st.info("Video tidak akan tampil sampai Anda mengganti URL di `app.py`.")
else:
    st.video(youtube_unlisted_url)

st.markdown("---")
