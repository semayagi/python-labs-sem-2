from src.infrastructure.logger import logger
from src.services.task_receiver import TaskReceiver
from src.sources.generator import GeneratorTaskSource
from src.sources.api import APITaskSource
from src.sources.json import JSONTaskSource
from src.models.task import Task

# For annotations, is it OK to use default "list" instead of "List" from typing lib?
def display_tasks(tasks: list[Task]): 
    print("==============")
    for task in tasks:
        print(f"ID: {task.id}, payload: {task.payload}, created_at: {task.created_at}, status: {task.status}")
    print("==============")

def main() -> None:
    '''
    Entry point of the application
    '''
    logger.info("Program started")
    print("Welcome to the Task Receiver application! Which task source do you choose?")

    receiver = TaskReceiver()
    while(True):
        print("1. Generated Task\n2. API\n3. JSON File\n4. Quit")
        choice = input("Enter your choice: ").strip()
        logger.info(f"User selected option: {choice}")
        match choice:
            case '1':
                count = input("Enter the count of tasks to generate: ")
                logger.info(f"User entered count of tasks to generate: {count}")
                if not (count.isdigit() and int(count) > 0):
                    print("Invalid input! Enter a positive integer!\n")
                    continue
                source = GeneratorTaskSource(int(count))
            case '2':
                source = APITaskSource()
            case '3':
                source = JSONTaskSource("json_source.json")
            case '4':
                break
            # The option to read several sources will be added later
            case _:
                logger.warning(f"User entered invalid option: {choice}")
                print("Invalid input! Input an integer from 1 to 5.\n")
        tasks = receiver.receive(source)
        display_tasks(tasks)


if __name__ == "__main__":
    main()
