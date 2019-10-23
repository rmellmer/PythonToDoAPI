from flask import Blueprint, jsonify
from ..dynamoAccess import ToDoContext

todo_api = Blueprint('todo_api', __name__)

@todo_api.route('/todos')
def getTodos():
    todo_client = ToDoContext()
    todos = todo_client.getTodos()
    return jsonify(todos)

@todo_api.route('/todo/<todoID>')
def getTodo(todoID):
    todo_client = ToDoContext()
    todo = todo_client.getTodo(todoID)
    return jsonify(todo)