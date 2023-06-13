import pickle

tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    print("Tasks: ")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}.{task}")

def update_task():
    view_tasks()
    task_index = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_index < len(tasks):
        new_task = input("Enter the new task: ")
        tasks[task_index] = new_task
        save_tasks()
        print("Task updated successfully!")
    else:
        print("Invalid Task Number!")

def delete_task():
    view_tasks()
    task_index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        save_tasks()
        print(f"Task '{deleted_task}' deleted successfully!")
    else:
        print("Invalid Task Number!")

def save_tasks():
    with open("tasks.pk1", "wb") as file:
        pickle.dump(tasks, file)

def load_tasks():
    global tasks
    try:
        with open("tasks.pk1", "rb") as file:
            tasks = pickle.load(file)
    except FileNotFoundError:
        tasks = []
    
def main():
    load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Tasks")
        print("4. Delete Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()