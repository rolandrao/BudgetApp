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
    path = os.path.join(f"exports/{st.session_state.filename}_export.csv")
    df.to_csv(path)