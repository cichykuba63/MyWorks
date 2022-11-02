list = ["make dinner", "clean up the flat"]

def show_tasks():
    index = 0
    print("\nYour tasks:\n")
    for task in list:
        index += 1
        print(f"{index}. {task.capitalize()}")

def add_task():
    task_describe = input("\nEnter a task you want to add: ")
    list.append(task_describe.lower())
    print("\nThe task was added successfully!")

def task_delete():
    pass

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
    if user_choice == 5:
        break

   


