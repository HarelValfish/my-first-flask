# from flask import Flask, jsonify, request
# from datetime import datetime, timezone

# app = Flask(__name__)
# @app.route('/')
# def home():
#     return jsonify({
#         "message": "API IS RUNNING!"
#     })
    
# @app.route('/status')
# def status():
#     return jsonify({
#         "status": "OK",
#         "version": "1.0.0"
#     })
    
# @app.route("/time")
# def time():
#     now = datetime.now(timezone.utc)
#     return jsonify({
#         "current_time": now.strftime("%Y-%m-%d %H:%M:%S")
#     })
    
# @app.route("/info")
# def info():
#     return jsonify({
#         "app_name": "My Flask API",
#         "description": "This is a simple Flask API for demonstration purposes.",
#         "author": "Your Name"
#     })
    
# @app.route("/echo", methods=["POST"])
# def echo():
#     body = request.json
#     return jsonify({
#         "success": True,
#         "message": body
#     })
    
# USERS = [
#     {"id": 1, "name": "Alice"},
#     {"id": 2, "name": "Bob"},
#     {"id": 3, "name": "Charlie"},
#     {"id": 4, "name": "Alice Smith"}
# ]

# @app.route("/search")
# def search():
#     name = request.args.get("name")
#     if not name:
#         return jsonify({
#             "success": False,
#             "error": "Missing 'name' query parameter"
#         }), 400
    
#     result = []
#     for u in USERS:
#         if name in u["name"]:
#             result.append(u)
    
#     return jsonify({
#         "success": True,
#         "results": result
#     })
    
# if __name__ == '__main__':
#     app.run(debug=True)