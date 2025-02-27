import time
import random
from persistent_queue.queue import Queue
from persistent_queue.sqlite_queue import SQLiteQueue

def simulate_crash(db_path='queue.db'):
    """
    Simulate a consumer crash after picking up a job.
    """
    db = SQLiteQueue(db_path)
    queue = Queue(db)

    # Submit a job
    job = {'id': 'crash_job', 'data': 'crash_data'}
    queue.enqueue(job)
    print("Job submitted:", job)

    # Dequeue the job (simulate consumer picking it up)
    dequeued_job = queue.dequeue()
    print("Job dequeued:", dequeued_job)

    # Simulate a crash (do not acknowledge the job)
    print("Simulating consumer crash...")
    time.sleep(2)  # Simulate some processing time
    print("Consumer crashed! Job will be requeued.")

    # Check if the job is requeued
    requeued_job = queue.dequeue()
    if requeued_job:
        print("Job requeued:", requeued_job)
    else:
        print("Job was not requeued.")

if __name__ == "__main__":
    simulate_crash()