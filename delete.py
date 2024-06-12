def delete_task(tasks, task_id):
    """Deletes a task from the task list based on task_id
    Args:
        tasks(list): List of tasks
        task_id(int): Task ID to be deleted
    """
    try:
        if not isinstance(tasks, list):
            raise ValueError("Tasks should be a list")
        if not isinstance(task_id, int):
            raise ValueError("Task ID should be an integer")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit()

    initial_len = len(tasks)
    tasks[:] = [task for task in tasks if task['task_id'] != task_id]

    if len(tasks) == initial_len:
        print(f"Task with ID {task_id} not found.")

# Example usage
tasks = []

add_task(tasks, 1, 34440, "buy a burger", "purchasing a burger tonight", "turn left on hello world", "14/05", "urgent")

for task in tasks:
    print(task)

# Delete the task
delete_task(tasks, 34440)

# Check if the task is deleted
for task in tasks:
    print(task)