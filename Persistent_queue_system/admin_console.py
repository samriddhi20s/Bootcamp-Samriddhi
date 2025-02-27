import streamlit as st
from persistent_queue.sqlite_queue import SQLiteQueue

# Initialize the database
db = SQLiteQueue('queue.db')

st.title('Admin Console')

# Display all jobs
jobs = db.get_all_jobs()
st.write('Pending Jobs:', jobs)

# Resubmit all failed jobs
if st.button('Resubmit All Failed Jobs'):
    dead_letter_jobs = db.get_all_dead_letter_jobs()
    for job in dead_letter_jobs:
        db.save_job(job)  # Resubmit the job to the main queue
        db.move_to_dead_letter_queue(job)  # Remove it from the dead letter queue
    st.write('Failed jobs resubmitted.')