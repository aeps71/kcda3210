import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly_express as px
import requests

st.set_page_config(layout='wide')

geojson_data = requests.get(
    "https://raw.githubusercontent.com/firmanh3200/batas-administrasi-indonesia/refs/heads/master/Kel_Desa/desa3210.json"
).json()

data = pd.read_csv(
    'data/penduduk3210.csv', sep=';',
    dtype={'id_desa':'str', 'total_pend':'float'}
)

data['KODE_KD'] = data['id_desa'].astype(str).str.slice(0, 2) + '.' + \
                   data['id_desa'].astype(str).str.slice(2, 4) + '.' + \
                   data['id_desa'].astype(str).str.slice(4, 6) + '.' + \
                   data['id_desa'].astype(str).str.slice(6, 10)

st.title("Peta Sebaran Penduduk Kabupaten Majalengka")
st.subheader("", divider='rainbow')

with st.container(border=True):
    kolom1, kolom2 = st.columns(2)
    data = data.sort_values(by=['tahun'], ascending=False)
    pilihantahun = data['tahun'].unique()
    pilihankec = data['kecamatan'].unique()
    pilihandesa = data['desa'].unique() 
    
    with kolom1:
        tahunterpilih = st.selectbox("Filter Tahun", pilihantahun)
    with kolom2:
       pilihkec = st.selectbox("Filter Kecamatan", pilihankec, key='kec1')    

    if tahunterpilih:
        st.subheader(f"Sebaran Penduduk di Kecamatan {pilihkec}, Tahun {tahunterpilih}")

        fig = px.choropleth_mapbox(
            data_frame=data[(data['tahun'] == tahunterpilih),
            geojson=geojson_data,
            locations="KODE_KD",
            color="total_pend",
            color_continuous_scale="Viridis_r",
            opacity=0.7,
            featureidkey="properties.KODE_KD",
            zoom=9,
            center={"lat": -6.836392508954653, "lon": 108.22905773884696},
            mapbox_style="carto-positron",
            hover_name="desa",
            hover_data=["kecamatan", "desa", 'tahun', "total_pend"]
        )

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)

st.subheader("", divider='rainbow')
st.link_button("Sumber Data", url="https://portaldatadesa.jabarprov.go.id/index-profile-desa/Sosial/Demografi")
st.link_button("Sumber Peta", url="https://github.com/Alf-Anas/batas-administrasi-indonesia") 
