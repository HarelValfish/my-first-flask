import uuid

tasks = [
    {"id": 1, "title": "Buy groceries", "completed": False},
    {"id": 2, "title": "Do homework", "completed": True},
    {"id": 3, "title": "Call mom", "completed": False}
]

def get_all_tasks():
    return tasks

def get_task_by_id(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

def create_task(task_data):
    new_task = {
        "id": uuid.uuid4(),
        "title": task_data['title'],
        "completed": False
    }
    tasks.append(new_task)
    return new_task