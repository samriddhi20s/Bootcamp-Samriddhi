import pytest
from persistent_queue.queue import Queue
from persistent_queue.sqlite_queue import SQLiteQueue

@pytest.fixture
def queue():
    db = SQLiteQueue(':memory:')
    return Queue(db)

def test_consumer_processes_job(queue):
    job = {'id': '1', 'data': 'test_data'}
    queue.enqueue(job)
    dequeued_job = queue.dequeue()
    assert dequeued_job == job
    queue.acknowledge(dequeued_job['id'])
    assert queue.dequeue() is None  # Queue should be empty after acknowledgment

def test_consumer_crash_requeues_job(queue):
    job = {'id': '1', 'data': 'test_data'}
    queue.enqueue(job)
    dequeued_job = queue.dequeue()
    queue.requeue(dequeued_job['id'])
    assert queue.dequeue() == job  # Job should be requeued