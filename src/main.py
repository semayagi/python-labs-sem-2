from src.sources.generator import GeneratorTaskSource
from src.sources.file import FileTaskSource
from src.sources.api import ApiTaskSource
from src.sources.json import JSONTaskSource
from src.services.task_receiver import TaskReceiver

def main() -> None:
    """
    Точка входа в приложение
    Демонстрация возможностей
    :return: Данная функция ничего не возвращает
    """

    receiver = TaskReceiver()

    source1 = GeneratorTaskSource(5)
    source2 = FileTaskSource("file_source_test.txt")
    source3 = ApiTaskSource()
    source4 = JSONTaskSource("json_source_test.json")

    tasks = receiver.receive(source1)
    for task in tasks:
        print(task)

    print("\n")
    tasks_from_many_sources = receiver.receive_many([source1, source2, source3, source4])
    for task in tasks_from_many_sources:
        print(task)


if __name__ == "__main__":
    main()
