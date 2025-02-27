import pytest
from persistent_queue.queue import Queue
from persistent_queue.sqlite_queue import SQLiteQueue

@pytest.fixture
def queue():
    db = SQLiteQueue(':memory:')  # Use in-memory SQLite for testing
    return Queue(db)

def test_producer_submits_job(queue):
    job = {'id': '1', 'data': 'test_data'}
    queue.enqueue(job)
    assert queue.dequeue() == job