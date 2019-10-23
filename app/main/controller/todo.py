import uuid
import time

from flask import Blueprint, jsonify, current_app, request
from app.main.dynamoAccess import ToDoContext

todo_api = Blueprint('todo_api', __name__)

# GET /todos - Gets all todos in the database
@todo_api.route('/todos')
def getTodos():
    todo_client = ToDoContext(current_app.config['TABLE_NAME'])
    todos = todo_client.getAll()
    if todos:
        return jsonify(dict(success = True, todos = todos))
    else:
        return createErrorJSON("Error querying database"), 500

# GET /todo/<todoID> - Get a specific todo by ID
@todo_api.route('/todo/<todoID>')
def getTodo(todoID):
    if todoID:
        todo_client = ToDoContext(current_app.config['TABLE_NAME'])
        todo = todo_client.get(todoID)
        if todo:
            return jsonify(dict(success = True, todo = todo))
        else:
            return createErrorJSON(f"Todo {todoID} not found"), 404
    else:
        return createErrorJSON("todoID not passed into URL (e.x.: /todo/<todoID>)"), 400

# POST /todo { message : 'todo message here' } - Add a todo
@todo_api.route('/todo', methods=['POST'])
def addTodo():
    todo = request.json
    if todo and 'message' in todo and todo['message'].strip():
        todo = {
            'todoID': str(uuid.uuid1()), # Create a UUID1 to serve as the todoID
            'timestamp': int("{:.3f}".format(time.time()).replace('.', '')), # Create a 13 digit integer representation of the current unix timestamp
            'message': todo['message'] # The passed-in message
        }
        todo_client = ToDoContext(current_app.config['TABLE_NAME'])
        todo_client.add(todo)
        return jsonify(todo)
    else:
        return createErrorJSON('Message not found or empty in input JSON'), 400

# DELETE /todo?todoID=<id>&timestamp=<timestamp> - Delete a todo by both todoID and timestamp (partition key and range key in DynamoDB)
@todo_api.route('/todo', methods=['DELETE'])
def deleteTodo():
    # Pull todoID and timestamp from url args, default to None if not passed in
    todoID = request.args.get('todoID', None)
    timestamp = request.args.get('timestamp', None)

    # Strip out any whitespace when checkig inputs
    if todoID and todoID.strip() and timestamp and timestamp.strip():
        todo_client = ToDoContext(current_app.config['TABLE_NAME'])
        deleted_todo = todo_client.delete(todoID, timestamp)
        if deleted_todo:
            return jsonify(dict(success = True, message = 'Deleted todo', todoID = deleted_todo['todoID']))
        else:
            return createErrorJSON("Todo not found"), 404
    else:
        return createErrorJSON("Must supply both the todoID and timestamp of the todo you wish to delete"), 400

def createErrorJSON(error_message):
    return jsonify(dict(success = False, message = error_message))