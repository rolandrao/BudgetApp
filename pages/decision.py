import streamlit as st
import pandas as pd



if 'df' not in st.session_state:
    st.session_state.df = None
if 'row_ind' not in st.session_state:
    st.session_state.row_ind = 0

df = st.session_state.df
row = df.iloc[[st.session_state.row_ind]]

if 'ts' not in st.session_state:
    st.session_state.ts = row['Timestamp'][0]
if 'cat' not in st.session_state:
    st.session_state.cat = row['Expense Category'][0]
if 'amt' not in st.session_state:
    st.session_state.amt = float(row['Amount'].iloc[0])
if 'who' not in st.session_state:
    st.session_state.who = row['Who Paid?']
if 'notes' not in st.session_state:
    st.session_state.notes = row['Notes'][0]
if 'finish' not in st.session_state:
    st.session_state.finish = True
if 'other_buttons' not in st.session_state:
    st.session_state.other_buttons = False


st.write("Make a decision about this expense below")
row_count = st.empty()
row_count.write(f"Row {st.session_state.row_ind+1} of {len(df)}")
ts = st.text_input("Timestamp", st.session_state.ts, key='ts')
notes = st.text_input("Notes", st.session_state.notes, key='notes')
cat = st.radio("Expense Category", [
    'Groceries', 
    'Shopping', 
    'Bills', 
    'Savings',
    'Transportation', 
    'Fun', 
    'Food', 
    'Uber Eats', 
    'Miscellaneous'
], index=None)
amt = st.number_input("Amount", st.session_state.amt, key='amt')
who = st.text_input("Who Paid?", "Roland")

def update(status):
    df.at[st.session_state.row_ind, 'Shared?'] = status

    df.at[st.session_state.row_ind, 'Timestamp'] = ts
    df.at[st.session_state.row_ind, 'Expense Category'] = cat
    df.at[st.session_state.row_ind, 'Amount'] = amt
    df.at[st.session_state.row_ind, 'Who Paid?'] = who
    df.at[st.session_state.row_ind, 'Notes'] = notes

    if st.session_state.row_ind != len(df)-1: 
        st.session_state.row_ind+=1
        print("Next Row")
    else: 
        print("Done")
        st.session_state.finish = False
        st.session_state.other_buttons = True

    print(st.session_state.row_ind)

    st.session_state.ts = df.iloc[st.session_state.row_ind]['Timestamp']
    st.session_state.cat = df.iloc[st.session_state.row_ind]['Expense Category']
    st.session_state.amt = df.iloc[st.session_state.row_ind]['Amount']
    st.session_state.who = df.iloc[st.session_state.row_ind]['Who Paid?']
    st.session_state.notes = df.iloc[st.session_state.row_ind]['Notes']

col1, col2, col3 = st.columns(3)

with col1:
    shared_button = st.button("Shared", on_click=update, args=('Yes',), disabled = st.session_state.other_buttons)

with col2:
    not_shared_button = st.button("Not Shared", on_click=update, args=('No',), disabled = st.session_state.other_buttons)

with col3:
    exclude_button = st.button("Exclude", on_click=update, args=('N/A',), disabled = st.session_state.other_buttons)

finish = st.button("Finish", disabled=st.session_state.finish)

if (shared_button or not_shared_button or exclude_button) and cat is None:
    st.warning("Please choose a category before deciding on this expense")

if finish:
    st.switch_page('pages/review.py')
