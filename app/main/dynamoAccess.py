import boto3
from boto3.dynamodb.conditions import Key, Attr

class ToDoContext:
    def __init__(self):
        dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
        self.table = dynamodb.Table('ToDos')

    def getTodos(self):
        todos = self.table.scan()

        if todos != None and 'Items' in todos:
            return todos['Items']
        else:
            return []
    
    def getTodo(self, todoID):
        todo = self.table.query(
            KeyConditionExpression=Key('todoID').eq(todoID)
        )

        if todo != None and 'Items' in todo and len(todo['Items']) > 0:
            return todo['Items'][0]
        else:
            return {}