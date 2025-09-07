#simple To-Do List Project

tasks = []

def show_menu():
    print("\n TO-DO LIST MENU")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        if not tasks:
            print("No tasks yet!")
        else:
            print("\nYour tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
    elif choice == '2':
        new_task = input("Enter a new task: ")
        tasks.append(new_task)
        print(f"Task '{new_task}' added!")
    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            task_num = input("Enter task number to remove: ")
            if task_num.isdigit() and 1 <= int(task_num) <= len(tasks):
                removed = tasks.pop(int(task_num)-1)
                print(f"Task '{removed}' removed!")
            else:
                print("Invalid task number.")
    elif choice == '4':
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1-4.")