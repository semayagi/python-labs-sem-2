from pathlib import Path
from src.sources.json import JSONTaskSource

def test_json_source():
    file = Path("tasks.json")
    file.write_text("""{
  "tasks": [
    { "id": "1", "payload": "asd" },
    { "id": "34", "payload": "sdsaf" }
  ]
}
""")

    source = JSONTaskSource(str(file))
    tasks = list(source.get_tasks())

    assert len(tasks) == 2
    assert tasks[0].id == 1