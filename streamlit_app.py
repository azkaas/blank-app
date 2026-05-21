import streamlit as st
import pandas as pd
import re

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Kalkulator Gravimetri",
    page_icon="⚗️",
    layout="wide"
)

# =====================================================
# DATA UNSUR KIMIA
# =====================================================

unsur = {
    "H": 1.008,
    "He": 4.0026,
    "Li": 6.94,
    "Be": 9.0122,
    "B": 10.81,
    "C": 12.011,
    "N": 14.007,
    "O": 15.999,
    "F": 18.998,
    "Ne": 20.180,
    "Na": 22.990,
    "Mg": 24.305,
    "Al": 26.982,
    "Si": 28.085,
    "P": 30.974,
    "S": 32.06,
    "Cl": 35.45,
    "K": 39.098,
    "Ca": 40.078,
    "Sc": 44.956,
    "Ti": 47.867,
    "V": 50.942,
    "Cr": 51.996,
    "Mn": 54.938,
    "Fe": 55.845,
    "Co": 58.933,
    "Ni": 58.693,
    "Cu": 63.546,
    "Zn": 65.38,
    "Ga": 69.723,
    "Ge": 72.630,
    "As": 74.922,
    "Se": 78.971,
    "Br": 79.904,
    "Kr": 83.798,
    "Rb": 85.468,
    "Sr": 87.62,
    "Ag": 107.868,
    "Cd": 112.414,
    "I": 126.904,
    "Ba": 137.327,
    "Pt": 195.084,
    "Au": 196.967,
    "Hg": 200.592,
    "Pb": 207.2
}

# =====================================================
# FUNGSI HITUNG Mr / BM
# =====================================================

def hitung_mr(rumus):
    pola = r'([A-Z][a-z]?)(\d*)'
    hasil = re.findall(pola, rumus)

    total = 0

    for simbol, jumlah in hasil:
        if simbol in unsur:
            jumlah = int(jumlah) if jumlah else 1
            total += unsur[simbol] * jumlah
        else:
            return None

    return total

# =====================================================
# JUDUL
# =====================================================

st.title("⚗️ Kalkulator Gravimetri")

st.markdown("""
Aplikasi perhitungan kimia berbasis Streamlit untuk membantu
analisis gravimetri dan perhitungan massa molekul relatif.
""")

st.markdown("---")

# =====================================================
# SIDEBAR MENU
# =====================================================

menu = st.sidebar.selectbox(
    "📂 Pilih Menu",
    ["Informasi", "Kalkulator", "Tabel Unsur"]
)

# =====================================================
# MENU INFORMASI
# =====================================================

if menu == "Informasi":

    st.header("📘 Informasi Analisis Gravimetri")

    st.subheader("1. Pengertian Analisis Gravimetri")

    st.write("""
    Analisis gravimetri merupakan metode analisis kuantitatif
    dalam kimia yang dilakukan dengan mengukur massa suatu zat.

    Pada metode ini, analit diubah menjadi bentuk endapan
    yang stabil kemudian ditimbang untuk menentukan kadar zat.
    """)

    st.subheader("2. Prinsip Analisis Gravimetri")

    st.write("""
    Prinsip dasar gravimetri meliputi:
    - Pembentukan endapan
    - Penyaringan endapan
    - Pencucian endapan
    - Pengeringan atau pemijaran
    - Penimbangan massa endapan
    """)

    st.subheader("3. Rumus Perhitungan Kadar")

    st.latex(r'''
    \%Kadar = \frac{massa\ analit}{massa\ sampel} \times 100\%
    ''')

    st.write("""
    Persen kadar digunakan untuk mengetahui banyaknya zat
    analit dalam suatu sampel.
    """)

    st.subheader("4. Pengertian Ar")

    st.write("""
    Ar (Atom Relatif) adalah massa atom suatu unsur dibandingkan
    terhadap 1/12 massa atom karbon-12.
    """)

    st.subheader("5. Pengertian Mr / BM")

    st.write("""
    Mr (Massa Molekul Relatif) atau BM (Berat Molekul)
    adalah jumlah seluruh Ar unsur-unsur penyusun senyawa.
    """)

    st.write("Contoh:")

    st.latex(r'''
    H_2SO_4 = (2 \times H) + (1 \times S) + (4 \times O)
    ''')

    st.write("""
    sehingga nilai Mr H₂SO₄ diperoleh dari penjumlahan seluruh Ar.
    """)

# =====================================================
# MENU KALKULATOR
# =====================================================

elif menu == "Kalkulator":

    st.header("🧪 Kalkulator Gravimetri")

    # -----------------------------------------
    # KALKULATOR Mr
    # -----------------------------------------

    st.subheader("🔬 Kalkulator Mr / BM")

    rumus = st.text_input(
        "Masukkan Rumus Kimia",
        placeholder="Contoh: H2SO4"
    )

    if st.button("Hitung Mr / BM"):

        hasil = hitung_mr(rumus)

        if hasil:
            st.success(f"Mr / BM {rumus} = {hasil:.3f}")
        else:
            st.error("Rumus kimia tidak valid.")

    st.markdown("---")

    # -----------------------------------------
    # PERHITUNGAN GRAVIMETRI
    # -----------------------------------------

    st.subheader("⚖️ Perhitungan Gravimetri")

    col1, col2 = st.columns(2)

    with col1:

        massa_sampel = st.number_input(
            "Massa Sampel (gram)",
            min_value=0.0,
            value=1.0
        )

        massa_endapan = st.number_input(
            "Massa Endapan (gram)",
            min_value=0.0,
            value=0.0
        )

    with col2:

        faktor_gravimetri = st.number_input(
            "Faktor Gravimetri",
            min_value=0.0,
            value=1.0
        )

    massa_analit = massa_endapan * faktor_gravimetri

    if massa_sampel > 0:
        persen_kadar = (massa_analit / massa_sampel) * 100
    else:
        persen_kadar = 0

    st.markdown("### ✅ Hasil")

    st.write(f"**Massa Analit = {massa_analit:.4f} gram**")
    st.write(f"**Persen Kadar = {persen_kadar:.2f}%**")

# =====================================================
# MENU TABEL UNSUR
# =====================================================

elif menu == "Tabel Unsur":

    st.header("🧬 Tabel Unsur Kimia dan Ar")

    df = pd.DataFrame({
        "Unsur": unsur.keys(),
        "Ar": unsur.values()
    })

    st.dataframe(df, use_container_width=True)

    st.info("""
    Tabel di atas berisi beberapa unsur kimia beserta
    nilai Ar (Atom Relatif) yang digunakan dalam
    perhitungan massa molekul relatif (Mr/BM).
    """)

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")
st.caption("⚗️ Dibuat menggunakan Streamlit dan Python")

