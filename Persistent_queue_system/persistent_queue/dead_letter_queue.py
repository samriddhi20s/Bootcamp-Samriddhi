from persistent_queue.interfaces import DatabaseInterface

class DeadLetterQueue:
    def __init__(self, database: DatabaseInterface):
        self.database = database

    def add_job(self, job):
        """
        Move a job to the dead letter queue.
        """
        self.database.move_to_dead_letter_queue(job)

    def get_all_jobs(self):
        """
        Retrieve all jobs from the dead letter queue.
        """
        return self.database.get_all_dead_letter_jobs()

    def resubmit_job(self, job_id):
        """
        Resubmit a job from the dead letter queue back to the main queue.
        """
        job = self.database.get_dead_letter_job(job_id)
        if job:
            self.database.save_job(job)
            self.database.remove_dead_letter_job(job_id)