# To-Do List Application

tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def delete_task():
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                del tasks[index]
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("No tasks to delete.")

def main():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()