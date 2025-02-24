import time
import uuid
import os
from persistent_queue.sqlite_queue import PersistentQSQLite

queue = PersistentQSQLite()

def generate_file():
    file_path = f"data/{uuid.uuid4()}.txt"
    with open(file_path, 'w') as f:
        f.write("Sample data")
    return file_path

def submit_job():
    file_path = generate_file()
    job_id = str(uuid.uuid4())
    queue.enqueue(job_id, {"file_path": file_path})
    print(f"Submitted job {job_id} for file {file_path}")

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    while True:
        submit_job()
        time.sleep(5)