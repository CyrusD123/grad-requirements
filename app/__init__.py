from flask import Flask, g
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session

# Initialization of Flask App
application = Flask(__name__)
application.config.from_object(Config)

# Create login manager from flask-login
login = LoginManager(application)
# Declare route to handle logins
login.login_view = 'login'

# Create Engine for interacting with database
DB_URI = application.config['SQLALCHEMY_DATABASE_URI']
engine = create_engine(DB_URI)
metadata = MetaData(engine)

@application.before_request
def before_request():
    # Session behaves similarly but with different methods (you have to commit a session)
    global session = Session(engine)
    
@application.after_request
def after_request(response):
    # Close session so that it returns to the engine's connection pool
    session.close()
    return response

# Import all other necessary python files (This will be the master file with all of the code imported)
# However, we run application.py for the final product, not __init__.py
from app import routes, models