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

class Student(db.Model):
    __tablename__ = 'requirements'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=False)
    last_name = db.Column('lname', db.Text, nullable=False)
    first_name = db.Column('fname', db.Text, nullable=False)
    class_year = db.Column('class', db.Integer, nullable=False)
    email = db.Column('email', db.Text, nullable=False)

    alg_score = db.Column('alg-score', db.Integer, nullable=True)
    alg_passing = db.Column('alg-passing', db.Boolean, nullable=False, default=True)
    alg_alt_assessment = db.Column('alg-alt-assessment', db.Boolean, nullable=False, default=False)
    alg_req_evidence = db.Column('alg-req-evidence', db.Integer, nullable=False, default=0)
    alg_add_evidence = db.Column('alg-add-evidence', db.Integer, nullable=False, default=0)
    alg_cte = db.Column('alg-cte', db.Boolean, nullable=False, default=False)
    alg_overall = db.Column('alg-overall', db.Boolean, nullable=False, default=False)

    lit_score = db.Column('lit-score', db.Integer, nullable=True)
    lit_passing = db.Column('lit-passing', db.Boolean, nullable=False, default=True)
    lit_alt_assessment = db.Column('lit-alt-assessment', db.Boolean, nullable=False, default=False)
    lit_req_evidence = db.Column('lit-req-evidence', db.Integer, nullable=False, default=0)
    lit_add_evidence = db.Column('lit-add-evidence', db.Integer, nullable=False, default=0)
    lit_cte = db.Column('lit-cte', db.Boolean, nullable=False, default=False)
    lit_overall = db.Column('lit-overall', db.Boolean, nullable=False, default=False)

    bio_score = db.Column('bio-score', db.Integer, nullable=True)
    bio_passing = db.Column('bio-passing', db.Boolean, nullable=False, default=True)
    bio_alt_assessment = db.Column('bio-alt-assessment', db.Boolean, nullable=False, default=False)
    bio_req_evidence = db.Column('bio-req-evidence', db.Integer, nullable=False, default=0)
    bio_add_evidence = db.Column('bio-add-evidence', db.Integer, nullable=False, default=0)
    bio_cte = db.Column('bio-cte', db.Boolean, nullable=False, default=False)
    bio_overall = db.Column('bio-overall', db.Boolean, nullable=False, default=False)

    composite_score = db.Column('composite-score', db.Integer, nullable=True, default=0)
    graduate_overall = db.Column('graduate-overall', db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return '<Student {}>'.format(self.id)