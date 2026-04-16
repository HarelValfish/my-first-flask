from flask import Flask, jsonify, request, Blueprint
from werkzeug.exceptions import NotFound, BadRequest
from models import get_all_tasks, get_task_by_id, create_task1, update_task_db

app = Flask(__name__)

tasks_bp = Blueprint('tasks', __name__)
#!======================GET ALL TASKS=========================

@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(get_all_tasks())

#!====================GET SINGLE TASK BY ID==========================

@tasks_bp.route('/tasks/<task_id>', methods=["GET"])
def get_task(task_id):
    task = get_task_by_id(task_id)
    if task:
        return jsonify(task)
    raise NotFound(f"Task with id '{task_id}' not found")

#!===================POST NEW TASK========================

@tasks_bp.route('/tasks', methods=["POST"])
def create_task():
    data = request.json
    if not data or 'title' not in data:
        raise BadRequest("Field 'title' is required")
    
    new_task = create_task1(data)
    return jsonify(new_task), 201

#!====================UPDATE TASK BY ID===========================

@tasks_bp.route('/tasks/<task_id>', methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    if not data:
        raise BadRequest("No data provided")

    updates = {}
    if 'title' in data:
        updates['title'] = data['title']
    if 'completed' in data:
        updates['completed'] = data['completed']
    
    updated_task = update_task_db(task_id, updates)
    if update_task:
        return jsonify(updated_task)
        
    raise NotFound(f"Task with id '{task_id}' not found")

#!=====================DELETE TASK BY ID=========================

@tasks_bp.route('/tasks/<task_id>', methods=["DELETE"])
def delete_task(task_id):
    for task in get_all_tasks:
        if task['id'] == task_id:
            get_all_tasks.remove(task)
            return jsonify({"message": "Task deleted"})
        
    raise NotFound(f"Task with id '{task_id}' not found")

#!========================================================

if __name__ == '__main__':
    app.run(debug=True)