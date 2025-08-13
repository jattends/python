my_tasks = {}
id = 1

def add_tasks(n):
    global my_tasks
    global id
    for t in range(n):
        task = input("Enter your task: ")
        if task:
            my_tasks[id] = {"task": task, "status": False}
            print(f"Added: ID={id}, Task='{task}'")
            id += 1
        else:
            print("Empty task not added.")

def update_task():
    if not my_tasks:
        print("No tasks available.")
        return
    try:
        update = int(input("Enter the task ID to mark as completed: "))
        if update in my_tasks:
            my_tasks[update]["status"] = True
            print(f"Task {update} will be  updated successfully.")
        else:
            print("Invalid task ID.")
    except ValueError:
        print("Please enter a valid integer ID.")

def delete_task():
    if not my_tasks:
        print("No tasks available to delete.")
        return
    try:
        tid = int(input("Enter the task ID to delete: "))
        if tid in my_tasks:
            removed = my_tasks.pop(tid)
            print(f"Deleted task {tid}: '{removed['task']}'")
        else:
            print("Invalid task ID.")
    except ValueError:
        print("Please enter a valid integer ID.")

def show_tasks():
    if not my_tasks:
        print("No tasks to show.")
    else:
        print("\nCurrent Tasks:")
        for tid, info in sorted(my_tasks.items()):
            status = "Done" if info["status"] else "Pending"
            print(f"ID {tid}: {info['task']} [{status}]")


while True:
    print("\none team project:")
    print("1. Add Tasks")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. Show Tasks")
    print("5. Exit")
    choice = input("Enter your choice (1–5): ")
    if choice == "1":
            n = int(input("How many tasks to add? "))
            if n > 0:
                add_tasks(n)
            else:
                print("Please enter a positive integer.")
            print("Please enter a number.")
    elif choice == "2":
        update_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        show_tasks()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
