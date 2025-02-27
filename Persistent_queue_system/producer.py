import sys
import os
import time
import uuid
from persistent_queue.queue import Queue
from persistent_queue.sqlite_queue import SQLiteQueue

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Initialize the database and queue
db = SQLiteQueue('queue.db')
queue = Queue(db)

def generate_file():
    """
    Generate a random file in the `data/` directory.
    """
    if not os.path.exists('data'):
        os.makedirs('data')  # Create the `data/` directory if it doesn't exist
    file_path = os.path.join('data', f'{uuid.uuid4()}.txt')
    with open(file_path, 'w') as f:
        f.write('Sample content')
    return file_path

def submit_job():
    """
    Submit a job to the queue.
    """
    file_path = generate_file()
    job = {'id': str(uuid.uuid4()), 'data': file_path}
    queue.enqueue(job)
    print(f"Submitted job: {job['id']}")

if __name__ == "__main__":
    while True:
        try:
            submit_job()
            time.sleep(5)  # Submit a job every 5 seconds
        except Exception as e:
            print(f"Error in producer: {e}")
            time.sleep(5)  # Wait before retrying