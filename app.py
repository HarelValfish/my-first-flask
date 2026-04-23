from flask import Flask, render_template
from database import init_db
from routes import tasks_bp
from errors import register_error_handlers

app = Flask(__name__)
init_db(app)
app.register_blueprint(tasks_bp)
register_error_handlers(app)

@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)