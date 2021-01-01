from app import login, session
from flask_login import UserMixin
from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash

# Declare base to create a table as mapped subclass of the base
base = declarative_base()

# The user inherits the functions of base and UserMixin
class User(base, UserMixin):
    # Map the class to the PostgreSQL table 'users'
    __tablename__ = 'users'
    id = Column('flask-id', Integer, primary_key=True, nullable=False)
    username = Column('username', Text, nullable=False)
    password_hash = Column('password-hash', Text, nullable=False)

    # __repr__ function describes the object
    def __repr__(self):
        return '<User {}>'.format(self.username)

    # Create functions for saving and storing hashed passwords using werkzeug
    # Assigns the hashed password to the User object (the object can be later committed to the database)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    # Checks the given plaintext password against the hashed one loaded from the User object
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Flask-login requires a user_loader route to load user objects based on their flask id
# Flask stores the key in memory as a string, so it must be converted to int
@login.user_loader
def load_user(id):
    return session.query(User).get(int(id))