from bson import ObjectId
from database import get_collection
from uuid import uuid4


def _todos_coll():
    return get_collection("todo")


def _serialize_task(task: dict) -> dict:
    task["_id"] = str(task["_id"])
    task.setdefault("subtasks", [])
    return task

#!=======================get all task func=========================

def get_all_tasks() :
    all_todos = list(_todos_coll().find({})) 
    for task in all_todos:
        _serialize_task(task)
    return all_todos

#!====================get task by id func=========================

def get_task_by_id(task_id: str) -> dict | None:
    try:
        task = _todos_coll().find_one({"_id": ObjectId(task_id)})
        
        if task:
            return _serialize_task(task)
            
        return None
    except Exception:
        return None
    
#!======================create task=========================

def create_task1(task_data):
    new_task = {
        "title": task_data['title'],
        "completed": False,
        "subtasks": []
    }
    result = _todos_coll().insert_one(new_task)
    new_task["_id"] = result.inserted_id
    return _serialize_task(new_task)

#!====================update task==========================

def update_task_db(task_id: str, update_data: dict):
    try:
        result = _todos_coll().update_one(
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
        result = _todos_coll().delete_one({"_id": ObjectId(task_id)})
        return result.deleted_count > 0
    except Exception:
        return False


def add_subtask_db(task_id: str, title: str):
    try:
        subtask = {
            "subtask_id": uuid4().hex,
            "title": title,
            "completed": False,
        }
        result = _todos_coll().update_one(
            {"_id": ObjectId(task_id)},
            {"$push": {"subtasks": subtask}},
        )
        if result.matched_count == 0:
            return None
        return get_task_by_id(task_id)
    except Exception:
        return None


def update_subtask_db(task_id: str, subtask_id: str, updates: dict):
    try:
        set_fields = {}
        if "title" in updates:
            set_fields["subtasks.$.title"] = updates["title"]
        if "completed" in updates:
            set_fields["subtasks.$.completed"] = updates["completed"]

        if not set_fields:
            return None

        result = _todos_coll().update_one(
            {"_id": ObjectId(task_id), "subtasks.subtask_id": subtask_id},
            {"$set": set_fields},
        )
        if result.matched_count == 0:
            return None
        return get_task_by_id(task_id)
    except Exception:
        return None


def delete_subtask_db(task_id: str, subtask_id: str):
    try:
        result = _todos_coll().update_one(
            {"_id": ObjectId(task_id)},
            {"$pull": {"subtasks": {"subtask_id": subtask_id}}},
        )
        return result.modified_count > 0
    except Exception:
        return False