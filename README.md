# PythonToDoAPI
Python Flask API to pull ToDos from DynamoDB

## Running locallaly using Flask
This project assumes that you're AWS CLI has been set up with permissions to access a DynamoDB table named "ToDos" (or whatever you configure in the config.py class)

To run the project, execute `python .\manage.py run`

To run unit tests, execute `python .\manage.py test`