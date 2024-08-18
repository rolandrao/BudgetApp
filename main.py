import pandas as pd
import streamlit as st
from datetime import datetime

if 'df' not in st.session_state:
    st.session_state.df = None
if 'month' not in st.session_state:
    st.session_state.month = None
if 'year' not in st.session_state:
    st.session_state.year = None

files = st.file_uploader("Upload a statement csv", accept_multiple_files=True)
dfs = []


preprocess = st.button('Preprocess')
if preprocess and files is not None:
    print(files)
    for file in files:
        print(f"Preprocessing {file.name}")
        df = pd.read_csv(file)
        if 'marriott' in file.name:
            df = df[df['Type'] != 'Payment']
            df = df[['Transaction Date', 'Description', 'Amount']]
        elif 'apple' in file.name:
            df = df[df['Type'] != 'Payment']
            df = df[['Transaction Date', 'Description', 'Amount (USD)']]
            df = df.rename(columns = {'Amount (USD)': 'Amount'})
        df['Expense Category'] = ''
        df['Shared?'] = ''
        df['Who Paid?'] = 'Roland'
        df = df.rename(columns = {
            'Transaction Date': 'Timestamp',
            'Description': 'Notes'
        })
        dfs.append(df)
        
    print(dfs)
    df_final = pd.concat(dfs, ignore_index=True)
    st.session_state.df = df_final
    st.dataframe(st.session_state.df)

month = st.selectbox('Month', [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
])



year = st.number_input('Year', value = datetime.now().year, step=1)
    


# if file is not None:
#     st.session_state.filename = file.name
#     df = pd.read_csv(file)
#     df['Shared'] = ''
#     df['Purchased By'] = 'Roland'
#     df = df[['Transaction Date', 'Category', 'Amount (USD)', 'Purchased By', 'Shared', 'Description']]
#     df = df.rename(columns = {
#         'Transaction Date': 'Timestamp',
#         'Category': 'Expense Category',
#         'Amount (USD)': 'Amount',
#         'Purchased By': 'Who Paid?',
#         'Shared': 'Shared?',
#         'Description': 'Notes'
#     })
#     st.session_state.df = df



next_button = st.button("Next Section")
if next_button:
    if st.session_state.df is not None and month is not None and year is not None:
        st.session_state.month = month
        st.session_state.year = year
        st.switch_page('pages/decision.py')



