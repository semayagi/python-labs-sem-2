from src.infrastructure.logger import logger
from src.sources.generator import GeneratorTaskSource
from src.sources.api import APITaskSource
from src.sources.json import JSONTaskSource
from src.models.task import Task, Status

from src.collections.task_queue import TaskQueue

# For annotations, is it OK to use default "list" instead of "List" from typing lib?
def display_tasks(tasks: list[Task]): 
    print("==============")
    for task in tasks:
        print(f"ID: {task.id}, description: {task.description}, priority: {task.priority}, created_at: {task.created_at}, deadline: {task.deadline}, status: {task.status}")
    print("==============")

def main() -> None:
    '''
    Entry point of the application
    '''
    logger.info("Program started")
    print("Welcome to the Task Receiver application!\nNEW FEATURE: Queue with filtration! Collect task sources into one queue and then iterate through it!")

    task_queue = TaskQueue()
    while(True):
        print("1. Generated Task\n2. API\n3. JSON File\n4. Show all tasks\n5. Iterate through task queue\n6. Set filtration\n7. Reset filtration\n8. Quit")
        choice = input("Enter your choice: ").strip()
        logger.info(f"User selected option: {choice}")
        match choice:
            case '1':
                count = input("Enter the count of tasks to generate: ")
                logger.info(f"User entered count of tasks to generate: {count}")
                if not (count.isdigit() and int(count) > 0):
                    print("Invalid input! Enter a positive integer!\n")
                    continue
                task_queue.add(GeneratorTaskSource(int(count)))
            case '2':
                task_queue.add(APITaskSource())
            case '3':
                task_queue.add(JSONTaskSource("json_source.json"))
            case '4':
                for task in task_queue:
                    print(task)
            case '5':
                for task in task_queue:
                    input(f"{task} > ")
            case '6':
                print("Leave blanks empty to choose no filtration.")
                print("Choose status filter:\n1. Pending\n2. In Progress\n3. Done\n4. Cancelled")
                status_choice = input("Choose status: ").strip()
                match status_choice:
                    case '1':
                        status_filter = Status.pending
                    case '2':
                        status_filter = Status.in_progress
                    case '3':
                        status_filter = Status.done
                    case '4':
                        status_filter = Status.cancelled
                    case _:
                        status_filter = None

                priority_choice = input("Choose priority filter (1-5): ").strip()
                if priority_choice.isdigit() and 1 <= int(priority_choice) <= 5:
                    priority_filter = int(priority_choice)
                else:
                    priority_filter = None

                task_queue.set_filtration(status_filter, priority_filter)
                print("Filtration set!")
            case '7':
                task_queue.reset_filtration()
                print("Filtration reset!")
                pass
            case '8':
                break

            # The option to read several sources will be added later
            case _:
                logger.warning(f"User entered invalid option: {choice}")
                print("Invalid input! Input an integer from 1 to 8.\n")

if __name__ == "__main__":
    main()
