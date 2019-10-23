import os
import unittest

from app.main import create_app
from flask_script import Manager

app = create_app(os.getenv('FLASK_ENV') or 'dev')
app.app_context().push()

manager = Manager(app)

@manager.command
def run():
    app.run()

@manager.command
def test():
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner().run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()