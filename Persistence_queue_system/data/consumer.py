import os
import time
import random
from persistent_queue.queue import Queue
from persistent_queue.sqlite_queue import SQLiteQueue

# Initialize the database and queue
db = SQLiteQueue('queue.db')
queue = Queue(db)

def process_job(job):
    """
    Process a job from the queue.
    """
    print(f"Processing job: {job['id']}")
    file_path = job['data']
    
    # Simulate processing delay
    time.sleep(random.randint(7, 15))
    
    # Delete the file after processing
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted file: {file_path}")
    
    # Acknowledge the job
    queue.acknowledge(job['id'])

def consume_jobs():
    """
    Continuously consume jobs from the queue.
    """
    while True:
        job = queue.dequeue()
        if job:
            try:
                process_job(job)
            except Exception as e:
                print(f"Job {job['id']} failed: {e}")
                queue.requeue(job['id'])
        time.sleep(1)

if __name__ == "__main__":
    consume_jobs()