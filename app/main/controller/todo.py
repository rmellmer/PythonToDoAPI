from flask import Blueprint, jsonify
from ..dynamoAccess import ToDoContext

todo_api = Blueprint('todo_api', __name__)

@todo_api.route('/todos')
def getTodos():
    todo_clent = ToDoContext()
    todos = todo_clent.getTodos()
    return jsonify(todos)