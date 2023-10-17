def load_tasks():
    tasks = []
    try:
        with open('tasks.txt', 'r') as file:
            for line in file:
                title, description, due_date, completed = line.strip().split('|')
                tasks.append({'title': title, 'description': description, 'due_date': due_date, 'completed': completed == 'True'})
    except FileNotFoundError:
        pass
    return tasks

def save_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(f"{task['title']}|{task['description']}|{task['due_date']}|{task['completed']}\n")

def add_task(tasks):
    title = input("Title: ")
    description = input("Description: ")
    due_date = input("Due Date (YYYY-MM-DD): ")
    tasks.append({'title': title, 'description': description, 'due_date': due_date, 'completed': False})
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, 1):
        print(f"{i}. Title: {task['title']}\n   Description: {task['description']}\n   Due Date: {task['due_date']}\n   Status: {'Complete' if task['completed'] else 'Incomplete'}")

def mark_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number to mark as complete: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number]['completed'] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number to delete: ")) - 1
        if 0 <= task_number < len(tasks):
            del tasks[task_number]
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Complete\n4. Delete Task\n5. Quit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
