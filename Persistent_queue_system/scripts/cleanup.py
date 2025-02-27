import os
import time

DATA_DIR = 'data'
MAX_AGE_SECONDS = 3600  # Delete files older than 1 hour

def cleanup_old_files():
    """
    Delete files in the data directory that are older than MAX_AGE_SECONDS.
    """
    current_time = time.time()
    for filename in os.listdir(DATA_DIR):
        file_path = os.path.join(DATA_DIR, filename)
        if os.path.isfile(file_path):
            file_age = current_time - os.path.getmtime(file_path)
            if file_age > MAX_AGE_SECONDS:
                os.remove(file_path)
                print(f"Deleted old file: {file_path}")

if __name__ == "__main__":
    cleanup_old_files()