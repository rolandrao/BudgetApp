import pandas as pd
import streamlit as st
from datetime import datetime

if 'df' not in st.session_state:
    st.session_state.df = None
if 'filename' not in st.session_state:
    st.session_state.filename = None

files = st.file_uploader("Upload a statement csv", accept_multiple_files=True)
dfs = []


who_paid = st.selectbox(label="Roommate", options=['Roland', 'Sarah'])
preprocess = st.button('Preprocess')
if preprocess and files is not None:
    print(files)
    for file in files:
        print(f"Preprocessing {file.name}")
        df = pd.read_csv(file)
        if 'marriott' in file.name:
            df = df[df['Type'] != 'Payment']
            df = df[['Transaction Date', 'Description', 'Amount']]
            df['Amount'] = df['Amount'] * -1
        elif 'apple' in file.name:
            df = df[df['Type'] != 'Payment']
            df = df[['Transaction Date', 'Description', 'Amount (USD)']]
            df = df.rename(columns = {'Amount (USD)': 'Amount'})
        elif 'capital_one' in file.name:
            df = df[df['Category'] != 'Payment/Credit']
            df = df[['Transaction Date', 'Description', 'Debit']]
            df = df.rename(columns = {'Debit': 'Amount'})
        df['Expense Category'] = ''
        df['Shared?'] = ''
        df['Who Paid?'] = who_paid
        df = df.rename(columns = {
            'Transaction Date': 'Timestamp',
            'Description': 'Notes'
        })
        df = df[['Timestamp', 'Expense Category', 'Amount', 'Who Paid?', 'Shared?', 'Notes']]
        dfs.append(df)
        
    df_final = pd.concat(dfs, ignore_index=True)
    print(df_final)
    st.session_state.df = df_final
    st.dataframe(st.session_state.df)






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
    if st.session_state.df is not None:
        st.session_state.filename = datetime.now().strftime("%m_%d_%Y__%H_%M_%S")
        st.switch_page('pages/decision.py')



