import pandas as pd
import streamlit as st

if 'df' not in st.session_state:
    st.session_state.df = None
if 'filename' not in st.session_state:
    st.session_state.filename = None

file = st.file_uploader("Upload a statement csv")
if file is not None:
    st.session_state.filename = file.name
    df = pd.read_csv(file)
    df['Shared'] = ''
    df['Purchased By'] = 'Roland'
    df = df[['Transaction Date', 'Category', 'Amount (USD)', 'Purchased By', 'Shared', 'Description']]
    df = df.rename(columns = {
        'Transaction Date': 'Timestamp',
        'Category': 'Expense Category',
        'Amount (USD)': 'Amount',
        'Purchased By': 'Who Paid?',
        'Shared': 'Shared?',
        'Description': 'Notes'
    })
    st.session_state.df = df



next_button = st.button("Next Section")
if next_button:
    if st.session_state.df is not None:
        st.switch_page('pages/decision.py')



