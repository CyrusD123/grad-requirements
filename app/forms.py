from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Email
from app.models import User, Student

# Create a class for the login form, inheriting the FlaskForm properties
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        # Exceptions for when username doesn't exist
        # Just a quick note, != and is not are not the same. Use 'is not' to check for None types
        if user is None:
            raise ValidationError('Username is incorrect. Please try again.')
    
    def validate_password(self, password):
        user = User.query.filter_by(username=self.username.data).first()
        # Checks if password is incorrect
        # User must exist to check for password, otherwise there is an error
        if user is not None and not user.check_password(password.data):
            raise ValidationError('Password is incorrect. Please try again.')

# Class for the registration form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    # Determines if the username already exists
    # The format validate_<fieldname> means that the function will be built into validate_on_submit
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username is already taken. Please try again.')

# Class for the registration form
class NewStudentForm(FlaskForm):
    id = IntegerField('Student ID', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    class_year = IntegerField('Graduating Class', validators=[DataRequired()])
    email = StringField('First Name', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')

    # Determines if the username already exists
    # The format validate_<fieldname> means that the function will be built into validate_on_submit
    def validate_id(self, id):
        student = Student.query.filter_by(username=id.data).first()
        if student is not None:
            raise ValidationError('Student ID is already taken. Please try again.')