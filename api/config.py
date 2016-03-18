# bucketlist/config.py

# import os, sys
# import inspect
# currentdir = os.path.dirname(os.path.abspath(
#     inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# sys.path.insert(0, parentdir)

# import os
# basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """Default Settings"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = "thequickbrownfoxjumpedoverthelazydog"


class DevelopmentConfig(Config):
    """setting Development configuration"""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bucketlists.db'
    DEBUG = True


class TestConfig(Config):
    """setting Testing configuration"""
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    TESTING = True