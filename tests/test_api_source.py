from src.sources.api import APITaskSource


def test_api_source():
    source = APITaskSource()
    tasks = list(source.get_tasks())

    assert len(tasks) == 2
    assert tasks[0].id == 100