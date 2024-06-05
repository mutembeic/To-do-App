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
        tasks, 1, 34440, "buy a burger", "purchasing a burger tonight",
        "turn left on hello world", "14/05", "urgent")

for task in tasks:
    print(task)
