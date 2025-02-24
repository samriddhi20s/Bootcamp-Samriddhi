import streamlit as st
from persistent_queue.sqlite_queue import PersistentQSQLite

queue = PersistentQSQLite()

st.title("Ops Console")

job_id = st.text_input("Enter Job ID")
if job_id:
    status = queue.get_status(job_id)
    st.write(f"Status of job {job_id}: {status}")

st.write("All Jobs")
cursor = queue.conn.cursor()
cursor.execute("SELECT job_id, status FROM jobs")
jobs = cursor.fetchall()
for job in jobs:
    st.write(f"Job ID: {job[0]}, Status: {job[1]}")