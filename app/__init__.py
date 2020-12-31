from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session

# Initialization of Flask App
application = Flask(__name__)
application.config.from_object(Config)

# Create Engine and Session for interacting with database
# They behave similarly but with different methods (you have to commit a session)
DB_URI = application.config['SQLALCHEMY_DATABASE_URI']
engine = create_engine(DB_URI)
session = Session(engine)
# Metadata is needed to fetch information about tables
metadata = MetaData(engine)

# Import all other necessary python files (This will be the master file with all of the code imported)
# However, we run application.py for the final product, not __init_.py
from app import routes