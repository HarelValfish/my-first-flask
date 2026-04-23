# My First Flask — Todo App

A full-stack task management app built with Flask and MongoDB. Supports tasks with nested subtasks, a dark-themed web UI, and a REST API.

## Features

- Create, edit, delete, and complete tasks
- Nested subtask management within each task
- Dark-themed, responsive frontend (vanilla JavaScript, no frameworks)
- REST API with proper validation and error handling
- XSS prevention via HTML escaping
- 16 pytest test cases with test database isolation

## Tech Stack

- **Backend:** Python / Flask
- **Database:** MongoDB (via pymongo)
- **Frontend:** Jinja2 templates, vanilla JavaScript, CSS
- **Testing:** pytest

## Project Structure

```
my-first-flask/
├── app.py              # App entry point
├── routes.py           # API route handlers (Flask Blueprint)
├── models.py           # CRUD operations / business logic
├── database.py         # MongoDB connection
├── errors.py           # Global error handlers
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Frontend UI
├── static/
│   └── style.css       # Dark theme styles
└── tests/
    ├── conftest.py
    └── test_tasks_api.py
```

## Setup

**Prerequisites:** Python 3.x, a MongoDB instance (local or Atlas)

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env  # then fill in your values
```

**.env file:**
```
MONGO_URI="mongodb+srv://<user>:<password>@<cluster>.mongodb.net/"
MONGO_DB="prod"
```

```bash
# Run the app
python app.py
```

App will be available at `http://localhost:5000`.

## API Reference

### Tasks

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/tasks` | List all tasks |
| `GET` | `/tasks/<id>` | Get a task |
| `POST` | `/tasks` | Create a task (`{ "title": "..." }`) |
| `PUT` | `/tasks/<id>` | Update a task (`title`, `completed`) |
| `DELETE` | `/tasks/<id>` | Delete a task |

### Subtasks

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/tasks/<id>/subtasks` | Add a subtask |
| `PUT` | `/tasks/<id>/subtasks/<subtask_id>` | Update a subtask |
| `DELETE` | `/tasks/<id>/subtasks/<subtask_id>` | Delete a subtask |

## Running Tests

```bash
pytest tests/ -v
```

Tests run against a separate `test` database.
