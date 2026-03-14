from pathlib import Path
from src.sources.file import FileTaskSource


def test_file_source():
    file = Path("tasks.txt")
    file.write_text("1,Samir\n2,is\n3,our\n4,favourite\n5,teacher!")

    source = FileTaskSource(str(file))
    tasks = list(source.get_tasks())

    assert len(tasks) == 5
    assert tasks[0].id == 1