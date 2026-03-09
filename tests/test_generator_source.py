from src.sources.generator_source import GeneratorTaskSource


def test_generator_source():
    source = GeneratorTaskSource(3)
    tasks = list(source.get_tasks())

    assert len(tasks) == 3
    assert tasks[0].id == 0