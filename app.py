from flask import Flask
from werkzeug.exceptions import NotFound, BadRequest, HTTPException
from routes import tasks_bp
from errors import errors_bp

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Buy groceries", "completed": False},
    {"id": 2, "title": "Do homework", "completed": True},
    {"id": 3, "title": "Call mom", "completed": False}
]

app.register_blueprint(tasks_bp)
app.register_blueprint(errors_bp)

if __name__ == '__main__':
    app.run(debug=True)