import sqlite3

def initialize_db(db_path='queue.db'):
    """
    Initialize the database and create necessary tables.
    """
    with sqlite3.connect(db_path) as conn:
        # Create the jobs table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                id TEXT PRIMARY KEY,
                data TEXT,
                status TEXT,
                retry_count INTEGER DEFAULT 0
            )
        ''')
        # Create the dead_letter_queue table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS dead_letter_queue (
                id TEXT PRIMARY KEY,
                data TEXT,
                status TEXT
            )
        ''')
    print(f"Database initialized at {db_path}")

if __name__ == "__main__":
    initialize_db()