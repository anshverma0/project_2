import argparse
import json
import os

# File to store tasks
TASK_FILE = "tasks.json"


# Load tasks from file
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return json.load(file)


# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


# Add a task
def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print(f"Task added: {description}")


# View tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✔️" if task["completed"] else "❌"
        print(f"{i}. {task['description']} [{status}]")


# Remove a task
def remove_task(index):
    tasks = load_tasks()
    try:
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task removed: {removed_task['description']}")
    except IndexError:
        print("Invalid task number.")


# Mark a task as completed
def complete_task(index):
    tasks = load_tasks()
    try:
        tasks[index - 1]["completed"] = True
        save_tasks(tasks)
        print(f"Task marked as completed: {tasks[index - 1]['description']}")
    except IndexError:
        print("Invalid task number.")


def main():
    parser = argparse.ArgumentParser(description="To-Do List Manager")
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Description of the task")

    # View command
    view_parser = subparsers.add_parser("view", help="View all tasks")

    # Remove command
    remove_parser = subparsers.add_parser("remove", help="Remove a task")
    remove_parser.add_argument("index", type=int, help="Task number to remove")

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as completed")
    complete_parser.add_argument("index", type=int, help="Task number to complete")

    # Parse arguments
    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "view":
        view_tasks()
    elif args.command == "remove":
        remove_task(args.index)
    elif args.command == "complete":
        complete_task(args.index)
    else:
        parser.print_help()
        print("finished project")


if __name__ == "__main__":
    main()
a=input("\n\n waiting")