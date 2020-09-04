"""
Author: Deividas Pelakauskas

"""

import datetime

class Task:

    def __init__(self, name, deadline, completed):
        self.name = name
        self.deadline = deadline
        self.completed = completed

def enter_date():
    """
    Enter date with validation

    :return: date in format of DD/MM/YYYY
    """
    while True:
        task_deadline = input("Enter date in following format - DD/MM/YYYY:\n")
        try:
            datetime.datetime.strptime(task_deadline, '%d/%m/%Y')
            return task_deadline
        except ValueError:
            print("Incorrect data format, should be DD/MM/YYYY")

def main():
    tasks = []
    tasks.append(Task("Task 1", "10/09/2020", False))
    tasks.append(Task("Task 2", "15/10/2021", False))

    menu_status = True
    while menu_status:
        option = input("1. View current tasks\n"
                       "2. Add new task\n"
                       "3. Delete task\n"
                       "0. Exit\n")

        if option == "1":
            if len(tasks) > 0:
                print("\n")
                print("DEADLINE\tTASK")
                for task in tasks:
                    print(task.deadline + "\t" + task.name)
                print("\n")
            else:
                print("Task list is empty")

        elif option == "2":
            task_name = input("Enter task name:\n")
            task_deadline = enter_date()
            tasks.append(Task(task_name, task_deadline, False))
            print("Successfully added new task")

        elif option == "3":
            pass

        elif option == "0":
            menu_status = False

        else:
            print("Unrecognised option")


main()
