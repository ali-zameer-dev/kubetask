from flask import Flask, jsonify, request
import uuid
import os

app = Flask(__name__)
tasks = {}

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "version": "1.0"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": list(tasks.values()), "count": len(tasks)})

@app.route('/tasks', methods=['POST'])
def create_task():
    body = request.json
    if not body.get('title'):
        return jsonify({"error": "Title required"}), 400
    task = {
        "taskId": str(uuid.uuid4()),
        "title": body["title"],
        "status": body.get("status", "pending"),
        "priority": body.get("priority", "medium")
    }
    tasks[task["taskId"]] = task
    return jsonify(task), 201

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id not in tasks:
        return jsonify({"error": "Not found"}), 404
    del tasks[task_id]
    return jsonify({"message": "Deleted"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
