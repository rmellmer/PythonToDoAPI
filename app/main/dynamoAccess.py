import boto3
from boto3.dynamodb.conditions import Key, Attr

class ToDoContext:
    def getTodos(self):
        dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
        table = dynamodb.Table('ToDos')

        todos = table.scan()

        if todos != None and 'Items' in todos:
            return todos['Items']
        else:
            return []