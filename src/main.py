from src.sources.generator import GeneratorTaskSource
from src.sources.file import FileTaskSource
from src.sources.api import APITaskSource
from src.sources.json import JSONTaskSource
from src.services.task_receiver import TaskReceiver

def main() -> None:
    '''
    Entry point of the application
    '''

    receiver = TaskReceiver()

    source1 = GeneratorTaskSource(5)
    source2 = FileTaskSource("file_source.txt")
    source3 = APITaskSource()
    source4 = JSONTaskSource("json_source.json")

    tasks = receiver.receive(source1)
    for task in tasks:
        print(task)

    print("\n")
    tasks_from_many_sources = receiver.receive_many([source1, source2, source3, source4])
    for task in tasks_from_many_sources:
        print(task)


if __name__ == "__main__":
    main()
