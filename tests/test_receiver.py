import pytest

from src.services.task_receiver import TaskReceiver
from src.models.task import Task
from typing import List


class BadSource:
    pass
    # не соответствует контракту

class NormalSource:
    # соответствует контракту
    def get_tasks(self) -> List[Task]:
        return [
            Task(id=123, payload={"ok": "data1"}),
            Task(id=321, payload={"ok": "data2"}),
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

    tasks1.extend(tasks2)
    assert tasks1 == receiver.receive_many([source1, source2])

def test_invalid_source():
    receiver = TaskReceiver()

    with pytest.raises(TypeError):
        receiver.receive(BadSource())

def test_many_invalid_source():
    receiver = TaskReceiver()

    with pytest.raises(TypeError):
        receiver.receive_many([NormalSource(), BadSource()])