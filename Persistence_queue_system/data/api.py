from fastapi import FastAPI, HTTPException
from persistent_queue.queue import Queue
from persistent_queue.sqlite_queue import SQLiteQueue

# Initialize the database and queue
db = SQLiteQueue('queue.db')
queue = Queue(db)

# Create a FastAPI app
app = FastAPI()

@app.post("/enqueue")
def enqueue(job: dict):
    """
    Enqueue a job into the queue.
    """
    if not job or 'id' not in job or 'data' not in job:
        raise HTTPException(status_code=400, detail="Invalid job data")
    queue.enqueue(job)
    return {"status": "success", "job_id": job['id']}

@app.get("/dequeue")
def dequeue():
    """
    Dequeue the next job from the queue.
    """
    job = queue.dequeue()
    if job:
        return job
    raise HTTPException(status_code=404, detail="No jobs available")

@app.post("/acknowledge/{job_id}")
def acknowledge(job_id: str):
    """
    Acknowledge a job as completed.
    """
    queue.acknowledge(job_id)
    return {"status": "success", "job_id": job_id}

@app.post("/requeue/{job_id}")
def requeue(job_id: str):
    """
    Requeue a failed job.
    """
    queue.requeue(job_id)
    return {"status": "success", "job_id": job_id}

@app.post("/dead_letter/{job_id}")
def move_to_dead_letter_queue(job_id: str):
    """
    Move a job to the dead letter queue.
    """
    queue.move_to_dead_letter_queue(job_id)
    return {"status": "success", "job_id": job_id}