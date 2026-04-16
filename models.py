from bson import ObjectId
from database import todos_coll

def get_all_tasks() -> list:
    all_todos = list(todos_coll.find({})) 
    for task in all_todos:
        task['_id'] = str(task['_id'])
    return all_todos

def get_task_by_id(task_id: str) -> dict | None:
    try:
        task = todos_coll.find_one({"_id": ObjectId(task_id)})
        
        if task:
            task['_id'] = str(task['_id'])
            return task
            
        return None
    except Exception:
        return None

def create_task1(task_data):
    new_task = {
        "title": task_data['title'],
        "completed": False
    }
    result = todos_coll.insert_one(new_task)
    new_task['_id'] = str(result.inserted_id)
    return new_task