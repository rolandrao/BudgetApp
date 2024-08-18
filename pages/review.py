import streamlit as st
import pandas as pd
import os
from googleapiclient.http import MediaFileUpload
from Google import Create_Service
import json



config = json.load('config.json')

service = Create_Service('client-secret.json', config['API_NAME'], config['API_VERSION'], config['SCOPES'] )

def download_file():
    path = os.path.join(f"exports/{st.session_state.month}_{st.session_state.year}_export.csv")
    df.to_csv(path)
    return path

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
