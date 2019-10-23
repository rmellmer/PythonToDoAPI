import unittest
from unittest import mock

from flask import current_app
from flask_testing import TestCase

from manage import app
from app.main.config import basedir

class TestAPI(TestCase):
    database_to_mock = "app.main.controller.todo.ToDoContext"

    def create_app(self):
        app.config.from_object('app.main.config.TestConfig')
        return app
    
    @mock.patch(database_to_mock)
    def test_get_all(self, mock_todocontext):
        # arrange
        test_todos = [ dict(todoID="b271", message="test todo"), dict(todoID="abcde", message="test todo # 2") ]
        mock_todocontext.return_value.getAll.return_value = test_todos

        # act
        response = app.test_client().get("/todos")

        # assert
        self.assert200(response)
        self.assertTrue(response.json['success'])
        self.assertEquals(response.json['todos'], test_todos)

    @mock.patch(database_to_mock)
    def test_get_one(self, mock_todocontext):
        # arrange
        test_id = "abcde"
        test_todo = dict(todoID=test_id, message="test todo")
        mock_todocontext.return_value.get.return_value = test_todo

        # act
        response = app.test_client().get(f"/todo/{test_id}")

        # assert
        self.assert200(response)
        self.assertTrue(response.json['success'])
        self.assertEquals(response.json['todo'], test_todo)

    @mock.patch(database_to_mock)
    def test_delete_success(self, mock_todocontext):
        # arrange
        test_id = "abcde"
        test_timestamp = 123456789
        test_todo = dict(todoID=test_id, timestamp=test_timestamp, message="test message")
        mock_todocontext.return_value.delete.return_value = test_todo

        # act
        response = app.test_client().delete(f"/todo?todoID={test_id}&timestamp={test_timestamp}")

        # assert
        self.assert200(response)
        self.assertEquals(response.json['todoID'], test_id)

    @mock.patch(database_to_mock)
    def test_delete_failure(self, mock_todocontext):
        # arrange
        test_id = "abcde"
        test_timestamp = 123456789
        mock_todocontext.return_value.delete.return_value = None

        # act
        response = app.test_client().delete(f"/todo?todoID={test_id}&timestamp={test_timestamp}")

        # assert
        self.assert404(response)
        self.assertEquals(response.json['success'], False)
