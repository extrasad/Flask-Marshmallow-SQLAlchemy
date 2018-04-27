import os

APP_DIR = os.path.abspath(os.path.dirname(__file__))
#STATIC_FOLDER = os.path.join('../', 'application/build')


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
#    STATIC_FOLDER = STATIC_FOLDER

#class ProdConfig(Config):
#    """Production configuration."""
#
#    ENV = 'prod'
#    DEBUG = False
#    SQLALCHEMY_DATABASE_URI = ''  
#    DEBUG_TB_ENABLED = False  


class DevelopmentConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    """Test configuration."""

    APP_VERSION = '0.0.1'
    TESTING = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False