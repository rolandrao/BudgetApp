import streamlit as st
import pandas as pd
import os


st.write("Review the spreadsheet before exporting")


if 'df' not in st.session_state:
    st.session_state.df = None
if 'filename' not in st.session_state:
    st.session_state.filename = None

df = st.session_state.df

st.dataframe(df)

export = st.button("Export")

if export:
    df = df[df['Shared?'] != 'N/A']
    path = os.path.join(f"exports/{st.session_state.filename[:-4]}_export.csv")
    df.to_csv(path)