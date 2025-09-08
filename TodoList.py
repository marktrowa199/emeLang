import os 

FILENAME = "tasks.txt"

#load tasks from file 
def load_tasks():
    if not os.path.exists(FILENAME):
        return[]
    with open(FILENAME, "r") as file:
        return [line.strip() for line in file.readlines()]

#save tasks to file 
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "/n")

#Menu display
def show_menu():
    print("\n TO-DO LIST MENU")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove task")
    print("4. Exit")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            if not tasks:
                print("No tasks yet!")
            else:
                print("\nYour tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
        elif choice == "2":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print(f"Task '{task}' added!")
        
        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
            else:
                task_num = input("Enter task number to remove: ")
                if task_num.isdigit() and 1 <= int(task_num) <= len(tasks):
                    removed = tasks.pop(int(task_num)-1)
                    save_tasks(tasks)
                    print(f"Task '{removed}' removed!")
                else:
                    print("Invalid task number.")
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()

