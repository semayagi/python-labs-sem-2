from src.sources.generator import GeneratorTaskSource
import datetime


def test_generator_source():
    source = GeneratorTaskSource(3)
    tasks = list(source.get_tasks())

    assert len(tasks) == 3
    assert tasks[0].id == "0"

    deadline: datetime.date = tasks[2].deadline

    assert deadline.year == 2029