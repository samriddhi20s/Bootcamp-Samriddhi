import sqlite3
from persistent_queue.interfaces import DatabaseInterface

class SQLiteQueue(DatabaseInterface):
    def __init__(self, db_path):
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS jobs (
                    id TEXT PRIMARY KEY,
                    data TEXT,
                    status TEXT,
                    retry_count INTEGER DEFAULT 0
                )
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS dead_letter_queue (
                    id TEXT PRIMARY KEY,
                    data TEXT,
                    status TEXT
                )
            ''')

    def save_job(self, job):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('INSERT INTO jobs (id, data, status) VALUES (?, ?, ?)', (job['id'], job['data'], 'pending'))

    def get_job(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('SELECT * FROM jobs WHERE status = ? LIMIT 1', ('pending',))
            row = cursor.fetchone()
            if row:
                return {'id': row[0], 'data': row[1], 'status': row[2], 'retry_count': row[3]}
            return None

    def requeue_job(self, job):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('UPDATE jobs SET status = ?, retry_count = ? WHERE id = ?', ('pending', job['retry_count'] + 1, job['id']))

    def move_to_dead_letter_queue(self, job):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('INSERT INTO dead_letter_queue (id, data, status) VALUES (?, ?, ?)', (job['id'], job['data'], 'failed'))
            conn.execute('DELETE FROM jobs WHERE id = ?', (job['id'],))

    def get_all_jobs(self):
        """
        Retrieve all jobs from the jobs table.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('SELECT * FROM jobs')
            rows = cursor.fetchall()
            return [{'id': row[0], 'data': row[1], 'status': row[2], 'retry_count': row[3]} for row in rows]

    def get_all_dead_letter_jobs(self):
        """
        Retrieve all jobs from the dead letter queue.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('SELECT * FROM dead_letter_queue')
            rows = cursor.fetchall()
            return [{'id': row[0], 'data': row[1], 'status': row[2]} for row in rows]