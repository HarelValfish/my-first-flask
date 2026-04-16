import uuid
from database import todos_coll, db

# tasks = [
#     {"id": 1, "title": "Buy groceries", "completed": False},
#     {"id": 2, "title": "Do homework", "completed": True},
#     {"id": 3, "title": "Call mom", "completed": False}
# ]

def get_all_tasks() -> list:
    # Use the collection object consistently
    all_todos = list(todos_coll.find({})) 
    for task in all_todos:
        # Convert ObjectId to string so Flask can jsonify it
        task['_id'] = str(task['_id'])
    return all_todos

def get_task_by_id(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

def create_task1(task_data):
    new_task = {
        "title": task_data['title'],
        "completed": False
    }
    result = todos_coll.insert_one(new_task)
    new_task['_id'] = str(result.inserted_id)
    return new_task