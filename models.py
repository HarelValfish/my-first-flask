from bson import ObjectId
from database import todos_coll
#!=======================get all task func=========================
def get_all_tasks() -> list:
    all_todos = list(todos_coll.find({})) 
    for task in all_todos:
        task['_id'] = str(task['_id'])
    return all_todos
#!====================get task by id func=========================
def get_task_by_id(task_id: str) -> dict | None:
    try:
        task = todos_coll.find_one({"_id": ObjectId(task_id)})
        
        if task:
            task['_id'] = str(task['_id'])
            return task
            
        return None
    except Exception:
        return None
#!======================create task=========================
def create_task1(task_data):
    new_task = {
        "title": task_data['title'],
        "completed": False
    }
    result = todos_coll.insert_one(new_task)
    new_task['_id'] = str(result.inserted_id)
    return new_task
#!====================update task==========================
def update_task_db(task_id: str, update_data: dict):
    try:
        result = todos_coll.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": update_data}
        )
        
        if result.matched_count > 0:
            return get_task_by_id(task_id)
        
        return None
    except Exception:
        return None
#!======================delete task=========================

def delete_task_db(task_id: str):
    try:
        result = todos_coll.delete_one({"_id": ObjectId(task_id)})
        return result.deleted_count > 0
    except Exception:
        return False