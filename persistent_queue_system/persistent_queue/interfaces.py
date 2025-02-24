from abc import ABC, abstractmethod

class PersistentQInterface(ABC):
    @abstractmethod
    def enqueue(self, job_id: str, job_data: dict):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def get_status(self, job_id: str):
        pass

    @abstractmethod
    def resubmit_job(self, job_id: str):
        pass

    @abstractmethod
    def mark_as_unprocessable(self, job_id: str):
        pass