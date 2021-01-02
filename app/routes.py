from app import application, engine, g.session, metadata
from app.models import User
from app.forms import LoginForm, RegistrationForm
from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy import Table

@application.route('/')
@application.route('/index')
@login_required
def index():
    return render_template('index.html')

@application.route('/login', methods=['GET', 'POST'])
def login():
    # Redirects user to homepage if they already signed in
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    # Create a LoginForm to pass to the template
    form = LoginForm()
    # validate_on_submit is one of the FlaskForm's methods
    if form.validate_on_submit():
        # Even though we arent explicityly instantiating a User class, .first() will return a single object (the first one in the table)
        # Which is defined by the __repr__ function of the User class, therefore creating a User object with User's methods
        user = session.query(User).filter_by(username=form.username.data).first()
        # Exceptions for when username doesn't exist or password is incorrect
        # Just a quick note, != and is not are not the same. Use 'is not' to check for None types
        if user is None or not user.check_password(form.password.data):
            # Flash a message which is handled in the template
            flash('Invalid username or password. Please try again.')
            return redirect(url_for('login'))
        # Log in the user using the built-in flask_login method
        login_user(user, remember=form.remember_me.data)
    return render_template('login.html', title='Login', form=form)

@application.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # Don't need to give the id because it is set to auto-increment (serial type) in PostgreSQL
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        print("after commit")
        session.add(user)
        print("after add")
        session.commit()
        print("after commit")
        # What does flash() do?
        #flash('You are now a registered user.')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@application.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))