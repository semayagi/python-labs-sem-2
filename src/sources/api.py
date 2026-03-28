import datetime
from typing import Iterable

from src.models.task import Task, Status

class APITaskSource:
    '''
    External API mock
    '''

    def get_tasks(self) -> Iterable[Task]:
        tasks = [
            Task(
                id="api-1",
                priority=1,
                deadline=datetime.date(2025, 6, 30),
                description="Process user data",
            ),
            Task(
                id="api-2",
                priority=3,
                deadline=datetime.date(2025, 7, 15),
                description="Fetch payment records",
            ),
            Task(
                id="api-3",
                priority=2,
                deadline=datetime.date(2027, 6, 14),
                description="Poll health check endpoint",
            ),
        ]
 
        tasks[1].status = Status.in_progress

        return tasks