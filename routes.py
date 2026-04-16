from flask import Flask, jsonify, request, Blueprint
from werkzeug.exceptions import NotFound, BadRequest, HTTPException
from models import get_all_tasks, get_task_by_id, create_task1
from database import db

app = Flask(__name__)

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(get_all_tasks())

@tasks_bp.route('/tasks/<task_id>', methods=["GET"])
def get_task(task_id):
    task = get_task_by_id(task_id)
    if task:
        return jsonify(task)
    raise NotFound(f"Task with id '{task_id}' not found")

@tasks_bp.route('/tasks', methods=["POST"])
def create_task():
    data = request.json
    if not data or 'title' not in data:
        raise BadRequest("Field 'title' is required")
    
    new_task = create_task1(data)
    return jsonify(new_task), 201

@tasks_bp.route('/tasks/<task_id>', methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    if not data:
        raise BadRequest("No data provided")
    
    for task in get_all_tasks:
        if task['id'] == task_id:
            if 'title' in data:
                task['title'] = data['title']
                
            if 'completed' in data:
                task['completed'] = data['completed']
                
            return jsonify(task)
        
    raise NotFound(f"Task with id '{task_id}' not found")

@tasks_bp.route('/tasks/<task_id>', methods=["DELETE"])
def delete_task(task_id):
    for task in get_all_tasks:
        if task['id'] == task_id:
            get_all_tasks.remove(task)
            return jsonify({"message": "Task deleted"})
        
    raise NotFound(f"Task with id '{task_id}' not found")

if __name__ == '__main__':
    app.run(debug=True)