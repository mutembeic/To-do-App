import sys

def search_task(tasks, task_id):
    """Finds a task based on it's task_id
    Args:
        tasks(list): List of tasks
        task_id(int): Task ID to be deleted
    """
    deleted_task = None
    tasks_copy = tasks.copy()

    try: 
        if not isinstance(tasks, list):
            raise ValueError("Tasks should be a list")
        if not isinstance(task_id, int):
            raise ValueError("Task ID should be an integer")
    except ValueError as e:
        print(f"Error: (e)")
        sys.exit()

    for task in tasks_copy:
        if task.get('task_id') == task_id:
            deleted_task = tasks_copy.remove(task)
            print(f"Task with ID {task_id} has been deleted.")
            break

        if task_id in task.values():
            pass

        else:
            print(f"Task with ID {task_id} not found.")

    return tasks_copy, deleted_task
