import pytest
from persistent_queue.interfaces import PersistentQInterface, DatabaseInterface

def test_persistent_q_interface():
    class TestQueue(PersistentQInterface):
        def enqueue(self, job):
            pass

        def dequeue(self):
            pass

        def acknowledge(self, job_id):
            pass

        def requeue(self, job_id):
            pass

        def move_to_dead_letter_queue(self, job_id):
            pass

    # Ensure the interface can be instantiated
    queue = TestQueue()
    assert isinstance(queue, PersistentQInterface)

def test_database_interface():
    class TestDatabase(DatabaseInterface):
        def save_job(self, job):
            pass

        def get_job(self):
            pass

        def requeue_job(self, job):
            pass

        def move_to_dead_letter_queue(self, job):
            pass

    # Ensure the interface can be instantiated
    db = TestDatabase()
    assert isinstance(db, DatabaseInterface)