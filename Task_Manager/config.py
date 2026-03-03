import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__)) # the root folder of the project
DB_PATH = os.path.join(BASE_DIR, 'instance', 'tasks.db') # the path to the base

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True # enables CSRF protection