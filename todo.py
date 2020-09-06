"""
Author: Deividas Pelakauskas

"""

from datetime import datetime


class Task:
    __last_id = 1

    def __init__(self, name, deadline, completed):
        self.name = name
        self.deadline = deadline
        self.completed = completed
        self.id = Task.__last_id
        Task.__last_id += 1


def enter_date():
    """
    Enter date with validation. Datetime module helps to check whether it is a valid day and month.

    :return: date in format of DD/MM/YYYY
    """
    while True:
        task_deadline = input("Enter date in following format - DD/MM/YYYY:\n")
        try:
            task_deadline_formatted = datetime.strptime(task_deadline, "%d/%m/%Y")  # Convert date in str to datetime for comparison
            current_date = datetime.today()  # To check if new task in not in the past date
            if task_deadline_formatted > current_date:
                return task_deadline
            else:
                print("Task date is in the past")
        except ValueError:
            print("Incorrect data format (DD/MM/YYYY) or other date related error")


def view_tasks(tasks, task_status):
    """
    Function to print tasks (used for pending and completed tasks)

    """
    counter = 0

    if len(tasks) > 0:
        print("\n")
        print("ID\tDEADLINE\tTASK")

        for task in tasks:
            if task.completed is not task_status:
                print(str(task.id) + "\t" + task.deadline + "\t" + task.name)
                counter += 1

        if task_status is True and counter == 0:
            print("There is no pending tasks")
        elif task_status is False and counter == 0:
            print("There is no completed tasks")

        print("\n")
    else:
        print("Task list is empty")


def check_task_exist(tasks, task_id_input):
    """
    Check if task with given task ID exists in list of tasks

    :param tasks: list of tasks
    :param task_id_input: id of the task
    :return: boolean value that determines whether task exists
    """
    return any(task.id == task_id_input for task in tasks)


def main():
    tasks = []

    # For testing
    tasks.append(Task("Task 1", "10/09/2020", False))
    tasks.append(Task("Task 2", "15/10/2021", False))

    menu_status = True  # To terminate the menu
    while menu_status:
        option = input("1. View current tasks\n"
                       "2. Add new task\n"
                       "3. Mark as completed\n"
                       "4. Delete task\n"
                       "5. View completed tasks\n"
                       "0. Exit\n")

        if option == "1":
            view_tasks(tasks, True)  # To view current pending tasks, True = pending tasks

        elif option == "2":
            task_name = input("Enter task name:\n")
            task_deadline = enter_date()
            tasks.append(Task(task_name, task_deadline, False))
            print("Successfully added new task")

        elif option == "3":
            try:
                task_id_input = int(input("Enter task ID\n"))

                if check_task_exist(tasks, task_id_input):  # Check if ID exists in list of tasks at all
                    for task in tasks:
                        if task_id_input == task.id and task.completed is False:
                            task.completed = True
                            print("Operation completed successfully")
                        elif task_id_input == task.id and task.completed is True:
                            print("Task with ID " + str(task_id_input) + " has already been marked as completed")
                else:
                    print("Task with ID " + str(task_id_input) + " does not exist")
            except ValueError:
                print("Invalid input")

        elif option == "4":
            try:
                task_id_input = int(input("Enter task ID\n"))

                if check_task_exist(tasks, task_id_input):  # Check if ID exists in list of tasks at all
                    for index, task in enumerate(tasks):  # Enumarate used to receive index
                        if task_id_input == task.id:
                            tasks.pop(index)
                            print("Task deleted successfully")
                else:
                    print("Task with ID " + str(task_id_input) + " does not exist")
            except ValueError:
                print("Invalid input")


        elif option == "5":
            view_tasks(tasks, False)  # To view already completed tasks, False = completed tasks

        elif option == "0":
            menu_status = False

        else:
            print("Unrecognised option")


main()
