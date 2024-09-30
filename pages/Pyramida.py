import streamlit as st

import numpy as np

# Data contoh piramida penduduk
# Usia (kelompok usia)
usia = ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65+']
# Jumlah penduduk laki-laki (negatif untuk membuat piramida)
laki_laki = [-500, -600, -800, -1000, -900, -700, -600, -400, -300, -200, -100, -50, -30, -20]
# Jumlah penduduk perempuan
perempuan = [480, 590, 780, 950, 920, 710, 590, 390, 290, 210, 120, 70, 50, 30]

# Membuat figure
fig, ax = plt.subplots(figsize=(10, 6))

# Membuat piramida penduduk
ax.barh(usia, laki_laki, color='blue', label='Laki-laki')
ax.barh(usia, perempuan, color='pink', label='Perempuan')

# Menambahkan label
ax.set_xlabel('Jumlah Penduduk')
ax.set_title('Piramida Penduduk')
ax.legend()

# Menambahkan grid
ax.grid(True)

# Menampilkan piramida di Streamlit
st.title("Piramida Penduduk")
st.pyplot(fig)
