import streamlit as st

st.set_page_config(
    page_title="Kalkulator Gravimetri",
    page_icon="⚗️",
    layout="centered"
)

st.title("⚗️ Kalkulator Gravimetri")
st.write("Aplikasi perhitungan gravimetri kimia berbasis Streamlit")

menu = st.sidebar.selectbox(
    "Pilih Menu",
    [
        "Hitung Persen Kadar",
        "Hitung Massa Endapan",
        "Hitung Massa Analit",
        "Hitung Faktor Gravimetri"
    ]
)

# =====================================================
# HITUNG PERSEN KADAR
# =====================================================

if menu == "Hitung Persen Kadar":

    st.header("📊 Perhitungan Persen Kadar")

    massa_analit = st.number_input(
        "Masukkan massa analit (gram)",
        min_value=0.0,
        format="%.4f"
    )

    massa_sampel = st.number_input(
        "Masukkan massa sampel (gram)",
        min_value=0.0,
        format="%.4f"
    )

    if st.button("Hitung Persen Kadar"):

        if massa_sampel > 0:
            persen = (massa_analit / massa_sampel) * 100

            st.success(f"Persen kadar = {persen:.2f}%")

            st.latex(r"\%\ Kadar = \frac{massa\ analit}{massa\ sampel} \times 100\%")

        else:
            st.error("Massa sampel tidak boleh nol")

# =====================================================
# HITUNG MASSA ENDAPAN
# =====================================================

elif menu == "Hitung Massa Endapan":

    st.header("🧪 Perhitungan Massa Endapan")

    massa_kertas = st.number_input(
        "Masukkan massa kertas saring kosong (gram)",
        min_value=0.0,
        format="%.4f"
    )

    massa_total = st.number_input(
        "Masukkan massa kertas + endapan (gram)",
        min_value=0.0,
        format="%.4f"
    )

    if st.button("Hitung Massa Endapan"):

        massa_endapan = massa_total - massa_kertas

        st.success(f"Massa endapan = {massa_endapan:.4f} gram")

        st.latex(r"massa\ endapan = massa\ total - massa\ kertas")

# =====================================================
# HITUNG MASSA ANALIT
# =====================================================

elif menu == "Hitung Massa Analit":

    st.header("⚖️ Perhitungan Massa Analit")

    massa_endapan = st.number_input(
        "Masukkan massa endapan (gram)",
        min_value=0.0,
        format="%.4f"
    )

    faktor = st.number_input(
        "Masukkan faktor gravimetri",
        min_value=0.0,
        format="%.6f"
    )

    if st.button("Hitung Massa Analit"):

        massa_analit = massa_endapan * faktor

        st.success(f"Massa analit = {massa_analit:.4f} gram")

        st.latex(r"massa\ analit = massa\ endapan \times faktor\ gravimetri")

# =====================================================
# HITUNG FAKTOR GRAVIMETRI
# =====================================================

elif menu == "Hitung Faktor Gravimetri":

    st.header("📘 Faktor Gravimetri")

    Mr_analit = st.number_input(
        "Masukkan Mr analit",
        min_value=0.0,
        format="%.4f"
    )

    Mr_endapan = st.number_input(
        "Masukkan Mr endapan",
        min_value=0.0,
        format="%.4f"
    )

    if st.button("Hitung Faktor"):

        if Mr_endapan > 0:
            faktor = Mr_analit / Mr_endapan

            st.success(f"Faktor gravimetri = {faktor:.6f}")

            st.latex(r"Faktor\ Gravimetri = \frac{Mr\ Analit}{Mr\ Endapan}")

        else:
            st.error("Mr endapan tidak boleh nol")

# =====================================================
# KALKULATOR Mr / BM SENYAWA
# =====================================================

st.markdown("---")
st.header("🧪 Kalkulator Mr / BM Senyawa")

unsur_lengkap = {
    "H": 1.008,
    "He": 4.003,
    "Li": 6.94,
    "Be": 9.012,
    "B": 10.81,
    "C": 12.01,
    "N": 14.01,
    "O": 16.00,
    "F": 19.00,
    "Ne": 20.18,
    "Na": 22.99,
    "Mg": 24.31,
    "Al": 26.98,
    "Si": 28.09,
    "P": 30.97,
    "S": 32.06,
    "Cl": 35.45,
    "Ar": 39.95,
    "K": 39.10,
    "Ca": 40.08,
    "Fe": 55.85,
    "Cu": 63.55,
    "Zn": 65.38,
    "Ag": 107.87,
    "Ba": 137.33,
    "Au": 196.97,
    "Hg": 200.59,
    "Pb": 207.2
}

rumus = st.text_input(
    "Masukkan rumus kimia (contoh: HCl, H2SO4, NaOH)",
    ""
)

import re


def hitung_mr(formula):
    pola = r'([A-Z][a-z]?)(\d*)'
    hasil = re.findall(pola, formula)

    total = 0

    for unsur, jumlah in hasil:
        if unsur in unsur_lengkap:
            jumlah = int(jumlah) if jumlah else 1
            total += unsur_lengkap[unsur] * jumlah
        else:
            return None

    return total


if st.button("Hitung Mr / BM"):

    mr = hitung_mr(rumus)

    if mr:
        st.success(f"Mr / BM {rumus} = {mr:.3f}")
    else:
        st.error("Rumus kimia tidak valid")

# =====================================================
# TABEL PERIODIK SEDERHANA
# =====================================================

st.markdown("---")
st.header("🧬 Data Unsur dan Ar Relatif")

unsur = {
    "H": 1.008,
    "He": 4.003,
    "Li": 6.94,
    "Be": 9.012,
    "B": 10.81,
    "C": 12.01,
    "N": 14.01,
    "O": 16.00,
    "F": 19.00,
    "Ne": 20.18,
    "Na": 22.99,
    "Mg": 24.31,
    "Al": 26.98,
    "Si": 28.09,
    "P": 30.97,
    "S": 32.06,
    "Cl": 35.45,
    "Ar": 39.95,
    "K": 39.10,
    "Ca": 40.08,
    "Sc": 44.96,
    "Ti": 47.87,
    "V": 50.94,
    "Cr": 52.00,
    "Mn": 54.94,
    "Fe": 55.85,
    "Co": 58.93,
    "Ni": 58.69,
    "Cu": 63.55,
    "Zn": 65.38,
    "Ga": 69.72,
    "Ge": 72.63,
    "As": 74.92,
    "Se": 78.97,
    "Br": 79.90,
    "Kr": 83.80,
    "Rb": 85.47,
    "Sr": 87.62,
    "Ag": 107.87,
    "Sn": 118.71,
    "I": 126.90,
    "Ba": 137.33,
    "Au": 196.97,
    "Hg": 200.59,
    "Pb": 207.2
}

pilih_unsur = st.selectbox(
    "Pilih unsur kimia",
    list(unsur.keys())
)

st.success(f"Ar {pilih_unsur} = {unsur[pilih_unsur]}")

st.dataframe(unsur.items())

st.markdown("---")
st.caption("Dibuat dengan Python dan Streamlit")
