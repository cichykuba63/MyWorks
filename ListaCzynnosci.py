list = []

def show_tasks():
    index = 0
    print("\nYour tasks:")
    for task in list:
        index += 1
        print(f"{index}. {task.capitalize()}")

def add_task():
    while True:
        task_describe = input("\nEnter a task you want to add: ")

        if task_describe == "" or task_describe.isspace() == True:
            print("Enter proper description")
            continue

        list.append(task_describe.lower())
        print("\nThe task was added successfully!")
        break

def task_delete():
    while True:
        choice = 0
        exception = False
        show_tasks()
        
        try:
            deleted_task = int(input("\nEnter the number of task you want to delete: "))
        except ValueError:
            print("Enter proper data.")
            continue

        for task in list:
            try:
                list.remove(list[deleted_task - 1])
                print("Your task has been deleted successfully!")
                break
            except IndexError:
                print("No such number was found.")
                exception = True
                break
        
        if exception == True:
            continue
        
        if len(list) != 0:
            while choice != "Y" and choice != "N":
                choice = input("\nDo you want to delete more task? (Y/N) > ")

                if choice.capitalize() == "Y":
                    break
                elif choice.capitalize() == "N":
                    print("Going back to menu...")
                    break
                else:
                    print("Enter proper data.")

            if choice.capitalize() == "N":
                break
        else:
            break

def save_tasks_to_file():
    file = open("tasks.txt", "w")
    
    for task in list:
        file.write(task + "\n")

    file.close()
    
    print("Tasks have been saved successfully!")

def read_tasks_from_file():
    try:
        file = open("tasks.txt")

        for line in file:
            list.append(line.strip())

        file.close()
    except FileNotFoundError:
        pass

read_tasks_from_file()
        
while True:
    user_choice = 0

    try:
        print("\nActivities:\n1. Show tasks.\n2. Add task.\n3. Delete task.\n4. Save tasks to file.\n5. Quit.")

        while user_choice != 1 and user_choice != 2 and user_choice != 3 and user_choice != 4 and user_choice != 5:
            user_choice = int(input("\nEnter number from 1 to 5: "))

            if user_choice != 1 and user_choice != 2 and user_choice != 3 and user_choice != 4 and user_choice != 5:
                print("Enter a number from 1 to 5!")
                print("\nActivities:\n1. Show tasks.\n2. Add task.\n3. Delete task.\n4. Save tasks to file.\n5. Quit.")
            
    except ValueError:
        print("Enter proper data.")
        continue

    if user_choice == 1:
        show_tasks()
    if user_choice == 2:
        add_task()
    if user_choice == 3:
        task_delete()
    if user_choice == 4:
        save_tasks_to_file()
    if user_choice == 5:
        break