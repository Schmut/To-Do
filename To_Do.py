# To Do List Program
print ("Welcome to your To Do list")

# Empty to do list 
# Empty completed list 
To_Do_List = []
Completed_List = []

# Print empty to do list & completed list
print (f"To do: {To_Do_List}")
print(f"Completed: {Completed_List}")

class Menu():
    # Pass init
    def __init__(self):
        pass

    def print_todo(self):
        print("To do:")
        for number, task in enumerate(To_Do_List,start=1):
            print(f"{number} | {task}")

    def print_completed(self):
        print("Completed:")
        for number,task in enumerate(Completed_List,start=1):
            print(f"{number} | {task}")
            
    # add task
    def add(add_task):
        add_task = input("What do you need to do?: ")
        To_Do_List.append(add_task)
        print("")
        Menu.print_todo(self=None)
        
    # Edit task
    def edit(edit_task):
        # Check if to do list is empty 
        if not To_Do_List:
            print("There is no task to edit")
        # Choose which task to edit 
        else:
            Menu.print_todo(self=None)
            edit_task = int(input("What task would you like to edit: "))
            edit_task -= 1
            print(To_Do_List[edit_task])
            edit_text = input("New entry: ")
            To_Do_List[edit_task] = edit_text
            Menu.print_todo
            
    def view(self):
        # Check if the to do list is empty 
        if not To_Do_List:
            print("There is nothing to do")
            pass
        # Show all items in to do list 
        else:
            Menu.print_todo(self=None)
            print("")
            Menu.print_completed(self=None)

    def complete(self):
        # Check if to do list is empty 
        if not To_Do_List:
            print("There is nothing to complete")
        else:
            Menu.print_todo(self=None)
            complete_task = int(input("What task would you like to complete: "))
            complete_task -= 1
            completed_task = To_Do_List.pop(complete_task)
            Completed_List.append(completed_task)
            print("")
            Menu.print_todo(self=None)
            print("")
            Menu.print_completed(self=None)
      
while True:
    option = input("""
Choose a choice
1. Add a task
2. Edit a task
3. View tasks 
4. Complete a task
10. Exit

Choice: """)
    if option == "1":
        print("")
        Menu.add(add_task=None)
    elif option == "2":
        print("")
        Menu.edit(edit_task=None)
    elif option == "3":
        print("")
        Menu.view(self=None)
    elif option == "4":
        Menu.complete(self=None)
    elif option == "10":
        break    