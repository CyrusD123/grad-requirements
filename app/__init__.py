from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialization of Flask App
application = Flask(__name__)
application.config.from_object(Config)

# Create login manager from flask-login
login = LoginManager(application)
# Declare route to handle logins
login.login_view = 'login'

# Create Engine and Session for interacting with database
# An engine is a pool of connections while sessions are individual connections
# They behave similarly but with different methods (you have to commit a session)
db = SQLAlchemy(application)

# Import all other necessary python files (This will be the master file with all of the code imported)
# However, we run application.py for the final product, not __init__.py
from app import routes, models