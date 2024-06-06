import sys
from datetime import datetime
"""
To-Do app
 --------
 It might be good to research efficient to-do's examples, read on the 
 literature.
 --------
 A todo list would need to have a:
 - a datastructure to hold the different tasks. I've opted for a list
   instead of an Object. We can refractor this later on into a class.
 - each task will be created as a dictionary, held within a list. 
 - Each task will have:
   -- id
   -- title
   -- description: a short summary
   -- notes: a longer description
   -- creation_date
   -- due_date
   -- completed - along with an automatic end date.
   -- priority

"""

def add_task(tasks, user_id, task_id, title, description, notes, 
             due_date, priority, completed=False):
    """Adds a task to the task list
    
    Args:
        tasks(list): List of tasks
        user_id(int): User ID
        task_id(int): Task ID
        title(str): Task title
        description(str): short summary of the task.
        notes(str): longer description of the task
        due_date(str): Due date of a task
        priority(str): one of: low, medium, high
        completed(bool, optional): Task completion status. Defaults to false.
    """

    try:
        if not isinstance(tasks, list):
            raise ValueError("Tasks should be a list")
        if not isinstance(user_id, int) or not isinstance(task_id, int):
            raise ValueError("User ID and Task ID should be integers")
        if not isinstance(title, str) or not isinstance(description, str):
            raise ValueError("title and/or description should be a string")
        if not isinstance(notes, str) or not isinstance(due_date, str):
            raise ValueError("notes and/or due_date should be a string")
        if not isinstance(priority, str):
            raise ValueError("priority should be a string")
        if not isinstance(completed, bool):
            raise ValueError("Completed should be a boolean")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit()

    task = {
            "user_id": user_id,
            "task_id": task_id,
            "title": title,
            "description": description,
            "notes": notes,
            "creation_date": datetime.now(),
            "due_date": due_date,
            "completed": completed,
            "priority": priority
            }

    tasks.append(task)

tasks = []

add_task(
        tasks, "1", 34440, "buy a burger", "purchasing a burger tonight",
        "turn left on hello world", "14/05", "urgent")

for task in tasks:
    print(task)
