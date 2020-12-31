import os

# Define the base directory for the configuration
basedir = os.path.abspath(os.path.dirname(__file__))

# Create a config class for the Flask app
class Config(object):
    # Create a random secret key that allows Flask to keep server communications secure
    SECRET_KEY = os.urandom(24)
    # We don't need SQLAlchemy to track modifications because it takes up memory
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Define the database url
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']