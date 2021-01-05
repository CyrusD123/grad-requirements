from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import login, db

# The user inherits the functions of base and UserMixin
class User(UserMixin, db.Model):
    # Map the class to the PostgreSQL table 'users'
    __tablename__ = 'users'
    id = db.Column('flask-id', db.Integer, primary_key=True)
    username = db.Column('username', db.Text, nullable=False)
    password_hash = db.Column('password-hash', db.Text, nullable=False)

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
    return User.query.get(int(id))