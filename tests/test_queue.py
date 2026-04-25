import datetime

from src.collections.task_queue import TaskQueue
from src.models.task import Status, Task


class DummyTaskSource:
    def __init__(self, tasks):
        self._tasks = tasks

    def get_tasks(self):
        return self._tasks


def make_task(task_id: str, status: Status = Status.pending, priority: int = 1):
    return Task(task_id, f"Task {task_id}", priority, datetime.datetime.now(), status=status)


def test_task_queue_iterates_all_sources_in_order():
    source1 = DummyTaskSource([make_task("a"), make_task("b")])
    source2 = DummyTaskSource([make_task("c")])
    queue = TaskQueue([source1, source2])

    assert list(queue) == [
        make_task("a"),
        make_task("b"),
        make_task("c"),
    ]


def test_task_queue_add_source_then_iterates_added_source():
    queue = TaskQueue()
    queue.add(DummyTaskSource([make_task("x")]))
    queue.add(DummyTaskSource([make_task("y")]))

    assert [task.id for task in queue] == ["x", "y"]


def test_task_queue_filters_by_status_and_priority():
    tasks = [
        make_task("1", status=Status.pending, priority=1),
        make_task("2", status=Status.done, priority=2),
        make_task("3", status=Status.pending, priority=2),
    ]
    queue = TaskQueue([DummyTaskSource(tasks)])
    queue.set_filtration(Status.pending, 2)

    assert [task.id for task in queue] == ["3"]


def test_task_queue_filters_by_priority_only():
    tasks = [
        make_task("1", status=Status.pending, priority=1),
        make_task("2", status=Status.done, priority=2),
        make_task("3", status=Status.pending, priority=2),
    ]
    queue = TaskQueue([DummyTaskSource(tasks)])
    queue.set_filtration(None, 2)

    assert [task.id for task in queue] == ["2", "3"]


def test_task_queue_reset_filtration_returns_all_tasks():
    tasks = [
        make_task("1", status=Status.pending, priority=1),
        make_task("2", status=Status.done, priority=2),
    ]
    queue = TaskQueue([DummyTaskSource(tasks)])
    queue.set_filtration(Status.done, 2)
    assert [task.id for task in queue] == ["2"]

    queue.reset_filtration()
    assert [task.id for task in queue] == ["1", "2"]
