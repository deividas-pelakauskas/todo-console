"""
Author: Deividas Pelakauskas

"""


class Task:

    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline


def main():
    menu_status = True
    while menu_status:
        option = input("1. View current tasks\n"
                       "2. Add new task\n"
                       "3. Delete task\n"
                       "0. Exit\n")

        if option == "1":
            pass

        elif option == "2":
            pass

        elif option == "3":
            pass

        elif option == "0":
            menu_status = False

        else:
            print("Unrecognised option")


main()
