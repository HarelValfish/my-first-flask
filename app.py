from flask import Flask, render_template
from routes import tasks_bp
from errors import errors_bp

app = Flask(__name__)

app.register_blueprint(tasks_bp)
app.register_blueprint(errors_bp)

@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)