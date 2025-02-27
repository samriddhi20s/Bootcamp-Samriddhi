import pytest
from persistent_queue.sqlite_queue import SQLiteQueue

@pytest.fixture
def db():
    return SQLiteQueue(':memory:')

def test_move_to_dead_letter_queue(db):
    job = {'id': '1', 'data': 'test_data'}
    db.save_job(job)
    db.move_to_dead_letter_queue(job)
    assert db.get_job() is None  # Job should be moved to dead letter queue