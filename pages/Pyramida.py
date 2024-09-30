import streamlit as st
import pandas as pd
import plotly_express as px
import openpyxl

datakk = pd.read_excel("data/penduduk_jk.xlsx")
sort_datakk = datakk.sort_values(by=['tahun', 'namakab', 'namakec', 'namadesa'], ascending=[False,True,True,True])

pilihankab = sort_datakk['namakab'].unique()

pilihantahun = sort_datakk['tahun'].unique()

base = alt.Chart(datakk).add_params(
    select_year
).transform_filter(
    select_year
).transform_calculate(
    gender=alt.expr.if_(alt.datum.sex == 1, 'Male', 'Female')
).properties(
    width=250
)


color_scale = alt.Scale(domain=['Male', 'Female'],
                        range=['#1f77b4', '#e377c2'])

left = base.transform_filter(
    alt.datum.gender == 'Female'
).encode(
    alt.Y('age:O').axis(None),
    alt.X('sum(people):Q')
        .title('population')
        .sort('descending'),
    alt.Color('gender:N')
        .scale(color_scale)
        .legend(None)
).mark_bar().properties(title='Female')

middle = base.encode(
    alt.Y('age:O').axis(None),
    alt.Text('age:Q'),
).mark_text().properties(width=20)

right = base.transform_filter(
    alt.datum.gender == 'Male'
).encode(
    alt.Y('age:O').axis(None),
    alt.X('sum(people):Q').title('population'),
    alt.Color('gender:N').scale(color_scale).legend(None)
).mark_bar().properties(title='Male')

alt.concat(left, middle, right, spacing=5)