from abc import ABC, abstractmethod

class PersistentQInterface(ABC):
    @abstractmethod
    def enqueue(self, job):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def acknowledge(self, job_id):
        pass

    @abstractmethod
    def requeue(self, job_id):
        pass

    @abstractmethod
    def move_to_dead_letter_queue(self, job_id):
        pass

class DatabaseInterface(ABC):
    @abstractmethod
    def save_job(self, job):
        pass

    @abstractmethod
    def get_job(self):
        pass

    @abstractmethod
    def requeue_job(self, job):
        pass

    @abstractmethod
    def move_to_dead_letter_queue(self, job):
        pass