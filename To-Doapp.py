#List in store tasks
tasks = []

#fuction to add task
def add_task():
    task = input("Enter your task:")
    tasks.append(task)
    print("Task added successfully!")

#function view tasks
def view_tasks():
    if len(tasks)==0:
        print("No tasks to show.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

#Program loop
def main():
    while True:
        print("To-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter Your choice:")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. please try again.\n")

if __name__ == "__main__":
    main()