from src.sources.api import ApiTaskSource


def test_api_source():
    source = ApiTaskSource()
    tasks = list(source.get_tasks())

    assert len(tasks) == 2
    assert tasks[0].id == 100