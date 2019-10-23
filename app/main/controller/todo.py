from flask import Blueprint, jsonify, current_app
from ..dynamoAccess import ToDoContext

todo_api = Blueprint('todo_api', __name__)

@todo_api.route('/todos')
def getTodos():
    todo_client = ToDoContext(current_app.config['TABLE_NAME'])
    todos = todo_client.getTodos()
    return jsonify(todos)

@todo_api.route('/todo/<todoID>')
def getTodo(todoID):
    todo_client = ToDoContext(current_app.config['TABLE_NAME'])
    todo = todo_client.getTodo(todoID)
    return jsonify(todo)