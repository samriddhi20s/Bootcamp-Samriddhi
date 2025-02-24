import streamlit as st
from persistent_queue.sqlite_queue import PersistentQSQLite

queue = PersistentQSQLite()

st.title("Admin Console")

job_id = st.text_input("Enter Job ID")
if job_id:
    if st.button("Resubmit Job"):
        queue.resubmit_job(job_id)
        st.write(f"Resubmitted job {job_id}")
    if st.button("Mark as Unprocessable"):
        queue.mark_as_unprocessable(job_id)
        st.write(f"Marked job {job_id} as unprocessable")