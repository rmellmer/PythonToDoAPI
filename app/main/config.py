import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False

class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):
    DEBUG = True
    TEST = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False

class ProdConfig(Config):
    DEBUG = False

config_by_name = dict(
    dev=DevConfig,
    test=TestConfig,
    prod=ProdConfig
)

key = Config.SECRET_KEY