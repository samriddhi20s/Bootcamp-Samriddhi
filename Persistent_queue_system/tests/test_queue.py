import pytest
from persistent_queue.queue import Queue
from persistent_queue.sqlite_queue import SQLiteQueue

@pytest.fixture
def queue():
    db = SQLiteQueue(':memory:')
    return Queue(db)

def test_enqueue_dequeue(queue):
    job = {'id': '1', 'data': 'test_data'}
    queue.enqueue(job)
    assert queue.dequeue() == job

def test_acknowledge_job(queue):
    job = {'id': '1', 'data': 'test_data'}
    queue.enqueue(job)
    dequeued_job = queue.dequeue()
    queue.acknowledge(dequeued_job['id'])
    assert queue.dequeue() is None  # Queue should be empty after acknowledgment

def test_requeue_job(queue):
    job = {'id': '1', 'data': 'test_data'}
    queue.enqueue(job)
    dequeued_job = queue.dequeue()
    queue.requeue(dequeued_job['id'])
    assert queue.dequeue() == job  # Job should be requeued

def test_move_to_dead_letter_queue(queue):
    job = {'id': '1', 'data': 'test_data'}
    queue.enqueue(job)
    dequeued_job = queue.dequeue()
    queue.move_to_dead_letter_queue(dequeued_job['id'])
    assert queue.dequeue() is None  # Job should be moved to dead letter queue