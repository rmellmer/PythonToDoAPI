import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

class ToDoContext:
    def __init__(self, table_name):
        dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
        self.table = dynamodb.Table(table_name)

    def getAll(self):
        try:
            todos = self.table.scan()
        except ClientError as e:
            if e.response['Error']['Code'] == "ConditionalCheckFailedException":
                print(e.response['Error']['Message'])
            return None

        if todos != None and 'Items' in todos:
            return todos['Items']
        else:
            return []
    
    def get(self, todoID):
        todo = self.table.query(
            KeyConditionExpression=Key('todoID').eq(todoID)
        )

        if todo != None and 'Items' in todo and len(todo['Items']) > 0:
            return todo['Items'][0]
        else:
            return None

    def add(self, todo):
        response = self.table.put_item(Item = todo)

    def delete(self, todoID, timestamp):
        key = {
            'todoID': todoID,
            'timestamp': int(timestamp)
        }
        
        try:
            response = self.table.delete_item(
                Key=key,
                ReturnValues='ALL_OLD'
            )

            if 'Attributes' in response:
                return response['Attributes']
            else:
                return None
        except ClientError as e:
            if e.response['Error']['Code'] == "ConditionalCheckFailedException":
                print(e.response['Error']['Message'])
            else:
                raise
