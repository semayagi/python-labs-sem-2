import pytest, datetime

from src.services.task_receiver import TaskReceiver
from src.models.task import Task
from typing import List

from src.infrastructure.logger import logger

# Violates the contract
class BadSource:
    pass
    
# Complies with the contract
class NormalSource:
    def get_tasks(self) -> List[Task]:
        return [
            Task(id=123, payload={
                "priority": 1,
                "deadline": datetime.date(2024, 10, 10),
                "description": "Money for nothing, Chicks for free"
            }),
            Task(id=321,  payload={
                "priority": 2,
                "deadline": datetime.date(2023, 1, 29),
                "description": "We gotta move these microwave ovens"
            }),
        ]


def test_valid_source():
    receiver = TaskReceiver()

    source = NormalSource()
    tasks = list(source.get_tasks())
    assert tasks == receiver.receive(source)

def test_many_valid_source():
    receiver = TaskReceiver()

    source1 = NormalSource()
    source2 = NormalSource()
    tasks1 = list(source1.get_tasks())
    tasks2 = list(source2.get_tasks())

    logger.info(f"Tasks1: {tasks1}")
    logger.info(f"Tasks2: {tasks2}")

    tasks1.extend(tasks2)
    logger.info(f"Extended tasks: {tasks1}")

    received_tasks = receiver.receive_many([source1, source2])
    logger.info(f"Received tasks: {received_tasks}")
    logger.info(f"{type(tasks1)}, {type(received_tasks)}")

    assert tasks1 == received_tasks

def test_invalid_source():
    receiver = TaskReceiver()

    with pytest.raises(TypeError):
        receiver.receive(BadSource())

def test_many_invalid_source():
    receiver = TaskReceiver()

    tasks = receiver.receive_many([NormalSource(), BadSource()])

    assert len(tasks) == 2  # BadSource skipped, NormalSource has 2 tasks