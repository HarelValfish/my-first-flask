from flask import jsonify, request, Blueprint
from werkzeug.exceptions import NotFound, BadRequest
from models import (
    get_all_tasks,
    get_task_by_id,
    create_task1,
    update_task_db,
    delete_task_db,
    add_subtask_db,
    update_subtask_db,
    delete_subtask_db,
)

tasks_bp = Blueprint('tasks', __name__)

# ============================================================
#  TASK ROUTES
# ============================================================

#! return all tasks
@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(get_all_tasks())


#! return a single task by ID
@tasks_bp.route('/tasks/<task_id>', methods=["GET"])
def get_task(task_id):
    task = get_task_by_id(task_id)
    if task:
        return jsonify(task)
    raise NotFound(f"Task with id '{task_id}' not found")


#! create a new task
@tasks_bp.route('/tasks', methods=["POST"])
def create_task():
    data = request.json
    if not data or 'title' not in data:
        raise BadRequest("Field 'title' is required")

    new_task = create_task1(data)
    return jsonify(new_task), 201


#! update a task's title and/or completed flag
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

    if not updates:
        raise BadRequest("No valid fields provided")

    updated_task = update_task_db(task_id, updates)
    if updated_task:
        return jsonify(updated_task)

    raise NotFound(f"Task with id '{task_id}' not found")


#! delete a task by ID
@tasks_bp.route('/tasks/<task_id>', methods=["DELETE"])
def handle_delete_task(task_id):
    success = delete_task_db(task_id)
    if success:
        return jsonify({"Message": "task deleted successfully"}), 200

    raise NotFound(f"Task with id '{task_id}' not found")


# ============================================================
#  SUBTASK ROUTES
# ============================================================

#! add a subtask to a task
@tasks_bp.route('/tasks/<task_id>/subtasks', methods=["POST"])
def create_subtask(task_id):
    data = request.get_json()
    if not data or 'title' not in data:
        raise BadRequest("Field 'title' is required")

    title = str(data['title']).strip()
    if not title:
        raise BadRequest("Subtask title cannot be empty")

    updated_task = add_subtask_db(task_id, title)
    if not updated_task:
        raise NotFound(f"Task with id '{task_id}' not found")

    return jsonify(updated_task), 201


#! update a subtask's title and/or completed flag
@tasks_bp.route('/tasks/<task_id>/subtasks/<subtask_id>', methods=["PUT"])
def update_subtask(task_id, subtask_id):
    data = request.get_json()
    if not data:
        raise BadRequest("No data provided")

    updates = {}
    if 'title' in data:
        title = str(data['title']).strip()
        if not title:
            raise BadRequest("Subtask title cannot be empty")
        updates['title'] = title

    if 'completed' in data:
        if not isinstance(data['completed'], bool):
            raise BadRequest("Subtask completed must be a boolean")
        updates['completed'] = data['completed']

    if not updates:
        raise BadRequest("No valid fields provided")

    updated_task = update_subtask_db(task_id, subtask_id, updates)
    if not updated_task:
        raise NotFound(f"Subtask with id '{subtask_id}' not found for task '{task_id}'")

    return jsonify(updated_task)


#! delete a subtask
@tasks_bp.route('/tasks/<task_id>/subtasks/<subtask_id>', methods=["DELETE"])
def delete_subtask(task_id, subtask_id):
    success = delete_subtask_db(task_id, subtask_id)
    if not success:
        raise NotFound(f"Subtask with id '{subtask_id}' not found for task '{task_id}'")
    return jsonify({"Message": "subtask deleted successfully"}), 200