from src.infrastructure.logger import logger
from typing import List, Iterable

from src.contracts.task_source import TaskSource
from src.models.task import Task

class TaskReceiver:
    '''
    Service for receiving tasks from different sources
    '''

    def receive(self, source: TaskSource) -> List[Task]:
        ''' Receive tasks from a single source '''
        if not isinstance(source, TaskSource): # Runtime contract check
            logger.error(f"The source {source.__class__.__name__} violates the TaskSource contract!")
            raise TypeError("The source violates the TaskSource contract!")
        
        result = list(source.get_tasks())
        logger.debug(f"From {source.__class__.__name__} received tasks: {result}")
        return result
    
    def receive_many(self, sources: Iterable[TaskSource]) -> List[Task]:
        ''' 
        Receive tasks from multiple sources
        Skips sources violating the TaskSource contract or failing unexpectedly
        '''
        tasks: List[Task] = []

        for source in sources:
            try:
                tasks.extend(self.receive(source))
            except TypeError as e:
                logger.warning(f"Skipping source {source.__class__.__name__} due to contract violation: {e}")
            # Btw, the following "except" block is considered untested by pytest-cov: (though IDK how to test UNEXPECTED errors)
            except Exception as e:
                logger.error(f"Unexpected error from source {source.__class__.__name__}: {e}")

        return tasks

