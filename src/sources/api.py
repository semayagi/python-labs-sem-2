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
                payload={
                    "priority": 1,
                    "deadline": datetime.date(2025, 6, 1),
                    "description": "Sync user data from remote API",
                },
            ),
            Task(
                id="api-2",
                payload={
                    "priority": 3,
                    "deadline": datetime.date(2025, 7, 15),
                    "description": "Fetch payment records",
                },
            ),
            Task(
                id="api-3",
                payload={
                    "priority": 2,
                    "deadline": None,
                    "description": "Poll health check endpoint",
                },
            ),
        ]
 
        tasks[1].status = Status.in_progress

        return tasks