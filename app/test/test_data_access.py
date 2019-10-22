import unittest
from unittest.mock import MagicMock

from flask import current_app
from flask_testing import TestCase

from manage import app
from app.main.config import basedir

class TestAPI(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.TestConfig')
        return app
    
    def test_get_all(self):
        response = self.client.get("/todos")
        print(response)
        self.assertEquals(response.json, dict(success=True))
        
