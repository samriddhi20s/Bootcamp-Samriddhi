from persistent_queue.interfaces import PersistentQInterface
from persistent_queue.sqlite_queue import SQLiteQueue

class Queue(PersistentQInterface):
    def __init__(self, database: SQLiteQueue, max_retries=3):
        self.database = database
        self.max_retries = max_retries
        self.in_progress_jobs = {}

    def enqueue(self, job):
        self.database.save_job(job)

    def dequeue(self):
        job = self.database.get_job()
        if job:
            self.in_progress_jobs[job['id']] = job
            return job
        return None

    def acknowledge(self, job_id):
        if job_id in self.in_progress_jobs:
            del self.in_progress_jobs[job_id]

    def requeue(self, job_id):
        if job_id in self.in_progress_jobs:
            job = self.in_progress_jobs[job_id]
            self.database.requeue_job(job)
            del self.in_progress_jobs[job_id]

    def move_to_dead_letter_queue(self, job_id):
        if job_id in self.in_progress_jobs:
            job = self.in_progress_jobs[job_id]
            self.database.move_to_dead_letter_queue(job)
            del self.in_progress_jobs[job_id]

    def check_timeouts(self):
        for job_id, job in list(self.in_progress_jobs.items()):
            if job['retry_count'] >= self.max_retries:
                self.move_to_dead_letter_queue(job_id)