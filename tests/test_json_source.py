from pathlib import Path
from src.sources.json import JSONTaskSource

def test_json_source():
    file = Path("tasks.json")
    file.write_text("""
      {
        "tasks": [
          {
            "id": "api-1",
            "priority": 1,
            "deadline": "2025-06-01",
            "description": "Sync user data from remote API"
          },
          {
            "id": "api-2",
            "priority": 3,
            "deadline": "2025-07-15",
            "description": "Fetch payment records"
          }
        ]
      }
      """)

    source = JSONTaskSource(str(file))
    tasks = list(source.get_tasks())

    assert len(tasks) == 2
    assert tasks[0].id == "api-1"