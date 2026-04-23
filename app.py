# brings in flask and the app's own modules for db, routes, and error handling
from flask import Flask, render_template
from database import init_db
from routes import tasks_bp
from errors import register_error_handlers

# creates the flask app, connects to mongo, and wires up blueprints and error handlers
app = Flask(__name__)
init_db(app)
app.register_blueprint(tasks_bp)
register_error_handlers(app)

# serves the main html page at the root url
@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

# only starts the dev server when the file is run directly, not when imported
if __name__ == '__main__':
    app.run(debug=True)