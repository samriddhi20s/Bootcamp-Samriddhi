import streamlit as st
from persistent_queue.sqlite_queue import SQLiteQueue

db = SQLiteQueue('queue.db')

st.title('Ops Console')
jobs = db.get_all_jobs()
st.write('Pending Jobs:', jobs)