# This is a to-do list app that allows users to add, remove, and view tasks.
# It uses a simple list to store the tasks in memory.
# This app is designed using Lists, Loops, and Conditional Statements.

# Blank list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

# Function to remove a task
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed from the list.")
    else:
        print(f"Task '{task}' not found in the list.")

# Function to view tasks
def view_tasks():
    if tasks:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks in the list.")

# Function to mark a task as completed
def mark_completed(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' marked as completed.")
    else:
        print(f"Task '{task}' not found in the list.")

# Main loop to run the app
def main():
    print("Welcome to the To-Do List App!")

    while True:
        print("\nEnter the command you want to execute:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. View tasks")
        print("4. Mark a task as completed")
        print("5. Exit")

        command = input("Enter a command (1-5): ")

        if command == "1":
            task = input("Enter the task to add: ")
            add_task(task)
        elif command == "2":
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif command == "3":
            view_tasks()
        elif command == "4":
            task = input("Enter the task to mark as completed: ")
            mark_completed(task)
        elif command == "5":
            print("Exiting the app.")
            break
        else:
            print("Invalid command. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
