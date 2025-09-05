# app.py
import streamlit as st
from PIL import Image
import requests

@st.cache_data
def load_and_rotate_image(url_or_path):
    """Fungsi untuk memuat dan memutar gambar dari URL atau file lokal."""
    if url_or_path.startswith("http"):
        # Jika URL, unduh gambar
        response = requests.get(url_or_path, stream=True)
        response.raise_for_status() # Pastikan request berhasil
        img = Image.open(response.raw)
    else:
        # Jika path lokal
        img = Image.open(url_or_path)

    # --- Bagian Penting untuk Memutar Gambar ---
    # Ganti metode di bawah ini sesuai kebutuhan Anda (ROTATE_180, FLIP_TOP_BOTTOM, dll.)
    rotated_img = img.transpose(Image.ROTATE_180)

    return rotated_img
# Mengatur konfigurasi dasar halaman web
st.set_page_config(
    page_title="Dashboard Saya",
    page_icon="🏠",
    layout="centered"
)

# --- Konten Halaman Dashboard ---
st.title("🎁IVA's BIRTHDAY")
st.write("🎉🎉 Selamat Ulang Tahun Iva 🎉🎉")

# Menambahkan pesan di sidebar
st.sidebar.success("Bioskop Disebelah Sini")
st.sidebar.markdown("---")


# Ganti URL gambar di bawah dengan URL gambar Anda sendiri
image_url = "20241208_183247.jpg"

# --- BLOK TRY-EXCEPT SEKARANG HANYA MEMANGGIL FUNGSI ---
try:
    # Panggil fungsi untuk memuat dan memutar gambar
    display_image = load_and_rotate_image(image_url)

    # Menampilkan gambar yang sudah diputar
    st.image(
        display_image,
        width=450
    )
except Exception as e:
    st.error(f"Gagal memuat atau memutar gambar: {e}")
    st.warning("Pastikan URL gambar valid dan dapat diakses.")


st.markdown("---")

# --- Bagian Ucapan ---
st.header("📝 Pesan Singkat")
st.write(
    """
Hari ini 26 tahun yang lalu, dunia dianugerahi mentari keduanya, Selamat Ulang Tahun!
Tersenyum cerahlah layaknya mentari di pagi hari, semoga kado kecil ini bisa jadi pengingat untuk tertawa 😁
Terimakasih sudah hadir di dunia dan tetap menjadi Iva
    """
)

# Menambahkan efek balon untuk menyambut pengguna
st.balloons()