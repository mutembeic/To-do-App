- I had a hard time reasoning about the list comprehension seen in your delete task function so I went a little more verbosity.

- I created a function to search for a specific task_id
- The idea behind the search function was to separate the searching from the deleting.
- I opted for making a copy of the list, returning it and the deleted task to avoid side effects from the original list.
- I'm not sure if returning the tasks_copy and deleted_task makes sense - the idea behind that was so it could be used in the delete function - which would then take those variables and ask for delete confirmation from the user. 
