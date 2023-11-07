
class UI:
    def __init__(self):
        print("__init__() method called ...")

    def print_menu(self):
        print("\t\tPeople Manager List Application")
        print ("\n")
        print("\t1. Add new person")
        print("\t2. List people")
        print("\t3. Delite Person")
        print("\t4. Exit")
        print("\n")


    def process_menu_choice(self):
        #print("proces_menu_choice() method called...")
        user_input= input("Enter Menu Choice: ")
        match(user_input):
            case "1": print("you entered 1")
            case _: print("invalid menu choice!")
