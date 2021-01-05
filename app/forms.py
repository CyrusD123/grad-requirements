from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo

# Create a class for the login form, inheriting the FlaskForm properties
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

# Class for the registration form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    # Determines if the username already exists
    # The format validate_<fieldname> means that the function will be built into validate_on_submit
    def validate_username(self, username):
        from app.routes import session
        if session.query(User).filter_by(username=username.data).first() is not None:
            raise ValidationError('Username is already taken. Please try again.')