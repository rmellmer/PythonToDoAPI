import unittest
from unittest import mock

from flask import current_app
from flask_testing import TestCase

from manage import app
from app.main.config import basedir

class TestAPI(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.TestConfig')
        return app
    
    @mock.patch("app.main.controller.todo.ToDoContext")
    def test_get_all(self, mock_todocontext):
        test_todos = [ dict(todoID="b271", message="test todo"), dict(todoID="abcde", message="test todo # 2") ]
        mock_todocontext.return_value.getTodos.return_value = test_todos
        response = app.test_client().get("/todos")

        self.assertEquals(response.json, test_todos)
        