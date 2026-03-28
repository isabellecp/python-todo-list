# todo list app in python

tasks = []

def show_menu():
    print("Welcome to the To-do list app. Please select an option:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Mark a task as completed")
    print("5. Exit")

def add_task():
        task = input("Enter a task: ")
        tasks.append({"task": task, "completed": False})
        print(f"task '{task}' added!")

def view_tasks():
        if not tasks:
            print("No tasks in the list.")
            return
        print("\nYour tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "✔️" if task["completed"] else "✖️"
            print(f"{index}. {task['task']} [{status}]")

def mark_done():
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark done ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print("Marked as completed!")
        else: 
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number!")

while True:
    show_menu()
    choice = input("Choose an option ('-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")


   
