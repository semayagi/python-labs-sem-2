from src.sources.api import APITaskSource
from src.models.task import Status


def test_api_source():
    source = APITaskSource()
    tasks = list(source.get_tasks())

    assert len(tasks) == 3
    assert tasks[0].id == "api-1"
    assert tasks[1].status == Status.in_progress