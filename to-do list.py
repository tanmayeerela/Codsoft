def to_do_list():
    tasks = []

    while True:
        print("\nTo-Do List Application")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Remove a task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter a new task: ")
            tasks.append(task)
            print(f"Task '{task}' added.")
        elif choice == '2':
            print("\nTasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == '3':
            task_number = int(input("Enter the task number to remove: "))
            if 0 < task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' removed.")
            else:
                print("Invalid task number.")
        elif choice == '4':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please choose again.")

to_do_list()
