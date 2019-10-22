import os
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app
from app.main.config import basedir

class TestDevConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.DevConfig')
        return app

    def test_app_is_dev(self):
        self.assertTrue(app.config['DEBUG'] is True)

class TestProdConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.ProdConfig')
        return app
    
    def test_app_is_prod(self):
        self.assertTrue(app.config['DEBUG'] is False)