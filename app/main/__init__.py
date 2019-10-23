import json
from flask import Flask
from flask.json import jsonify

from app.main.config import config_by_name
from app.main.controller.todo import todo_api
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.register_blueprint(todo_api)
    app.json_encoder = DecimalEncoder
    return app