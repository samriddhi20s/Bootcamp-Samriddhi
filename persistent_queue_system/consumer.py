import time
import random
from persistent_queue.sqlite_queue import PersistentQSQLite

queue = PersistentQSQLite()

def process_job(job_id, job_data):
    file_path = job_data['file_path']
    with open(file_path, 'r') as f:
        lines = f.readlines()
    with open(file_path, 'w') as f:
        for line in lines:
            f.write(f"{time.time()}: {line}")
    print(f"Processed job {job_id} for file {file_path}")

if __name__ == "__main__":
    while True:
        job = queue.dequeue()
        if job:
            job_id, job_data = job
            try:
                process_job(job_id, job_data)
                queue.mark_as_unprocessable(job_id)
            except Exception as e:
                print(f"Failed to process job {job_id}: {e}")
                queue.resubmit_job(job_id)
        time.sleep(random.randint(7, 15))