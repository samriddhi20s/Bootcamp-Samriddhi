import sqlite3
import os
from persistent_queue.interfaces import PersistentQInterface

class PersistentQSQLite(PersistentQInterface):
    def __init__(self, db_path='queue.db'):
        # Ensure the directory exists
        db_dir = os.path.dirname(db_path)
        if db_dir:  # If db_path includes a directory
            os.makedirs(db_dir, exist_ok=True)

        # Connect to the SQLite database
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                job_id TEXT PRIMARY KEY,
                job_data TEXT,
                status TEXT DEFAULT 'pending',
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def enqueue(self, job_id: str, job_data: dict):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO jobs (job_id, job_data) VALUES (?, ?)
        ''', (job_id, str(job_data)))
        self.conn.commit()

    def dequeue(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT job_id, job_data FROM jobs WHERE status = 'pending' ORDER BY timestamp LIMIT 1
        ''')
        job = cursor.fetchone()
        if job:
            job_id, job_data = job
            cursor.execute('''
                UPDATE jobs SET status = 'processing' WHERE job_id = ?
            ''', (job_id,))
            self.conn.commit()
            return job_id, eval(job_data)
        return None

    def get_status(self, job_id: str):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT status FROM jobs WHERE job_id = ?
        ''', (job_id,))
        status = cursor.fetchone()
        return status[0] if status else None

    def resubmit_job(self, job_id: str):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE jobs SET status = 'pending' WHERE job_id = ?
        ''', (job_id,))
        self.conn.commit()

    def mark_as_unprocessable(self, job_id: str):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE jobs SET status = 'unprocessable' WHERE job_id = ?
        ''', (job_id,))
        self.conn.commit()