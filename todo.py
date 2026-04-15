from flask import Flask, request, jsonify
import uuid
from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity

app = Flask(__name__)

todos = [{
    "id": 1,
    "title": "this_is_th_title",
    "is_completed": True
}]

next_id = 1

@app.errorhandler(TypeError)
def handle_type_error(e):
    return jsonify({
        "error": str(e)
    }), 400
    
@app.errorhandler(NotFound)
def handle_type_error(e):
    return jsonify({
        "error": str(e)
    }), 400
    
@app.errorhandler(BadRequest)
def handle_type_error(e):
    return jsonify({
        "error": str(e)
    }), 400
    
@app.errorhandler(UnprocessableEntity)
def handle_type_error(e):
    return jsonify({
        "error": str(e)
    }), 400



@app.route("/todo", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/todo", methods=["POST"])
def create_todo():
    # try:
        data = request.get_json()
        
        if data == {}:
            raise BadRequest("the request body most be JSON")
        
        title = data["title"]
        
        if not isinstance(title, str):
            raise BadRequest("title must be a string")
        
        if not title.strip():
            raise UnprocessableEntity("string cannot be empty or without spaces")
        
        new_todo = {
            "id": str(uuid.uuid4()),
            "title": title,
            "is_completed": False
        }
        
        todos.append(new_todo)
        return jsonify({
            "success": True,
            "new todo is: ": new_todo
        }), 200
        
if __name__ == "__main__":
    app.run(debug=True)