import pandas as pd
import streamlit as st

if 'df' not in st.session_state:
    st.session_state.df = None

file = st.file_uploader("Upload a statement csv")
if file is not None:
    df = pd.read_csv(file)
    st.session_state = df



next_button = st.button("Next Section")
if next_button:
    if st.session_state.df is not None:
        st.switch_page('pages/decision.py')



