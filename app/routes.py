from flask import Flask, g, jsonify, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import application, db
from app.models import User
from app.forms import LoginForm, RegistrationForm

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
        user = User.query.filter_by(username=form.username.data).first()
        # Exceptions for when username doesn't exist or password is incorrect
        # Just a quick note, != and is not are not the same. Use 'is not' to check for None types
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('login'))
        # Log in the user using the built-in flask_login method
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)

@application.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # Don't need to give the id because it is set to auto-increment (serial type) in PostgreSQL
        user = User(username=form.username.data)
        print("after username")
        user.set_password(form.password.data)
        print("after password")
        db.session.add(user)
        print("after add")
        db.session.commit()
        #print("after commit")
        db.session.close()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@application.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))