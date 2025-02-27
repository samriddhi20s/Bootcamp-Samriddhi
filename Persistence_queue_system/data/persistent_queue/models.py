from dataclasses import dataclass
from typing import Any

@dataclass
class Job:
    """
    Represents a job in the queue.
    """
    id: str
    data: Any
    status: str = "pending"
    retry_count: int = 0

    def is_timed_out(self):
        """
        Check if the job has timed out based on retry count.
        """
        return self.retry_count >= 3  # Example: 3 retries allowed