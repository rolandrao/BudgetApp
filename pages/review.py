import streamlit as st
import pandas as pd

if 'filename' not in st.session_state:
    st.session_state.filename = None

def download_file():
    path = f"exports/{st.session_state.filename}_export.csv"
    df.to_csv(path)

st.write("Review the spreadsheet before exporting")


if 'df' not in st.session_state:
    st.session_state.df = None
if 'filename' not in st.session_state:
    st.session_state.filename = None

df = st.session_state.df

st.dataframe(df)

download = st.button("Download")

if download:
    download_file()
