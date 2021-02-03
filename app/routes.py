from flask import Flask, g, jsonify, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import application, db
from app.models import User, Student
from app.forms import LoginForm, RegistrationForm, NewStudentForm, MainForm

@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = MainForm()
    if form.validate_on_submit():
        print('foo')
        print(form.base_form.entries)
    return render_template('index.html', form=form)

@application.route('/login', methods=['GET', 'POST'])
def login():
    # Redirects user to homepage if they already signed in
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    # Create a LoginForm to pass to the template
    form = LoginForm()
    # validate_on_submit is one of the FlaskForm's methods
    if request.method == "POST":
        if form.validate_on_submit():
            # Even though we arent explicityly instantiating a User class, .first() will return a single object (the first one in the table)
            # Which is defined by the __repr__ function of the User class, therefore creating a User object with User's methods
            user = User.query.filter_by(username=form.username.data).first()
            # Log in the user using the built-in flask_login method
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)

# Register requires you to already be authenticated, meaning that there always be one user to create new users
@application.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print("form validated")
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

@application.route('/new_student', methods=['GET', 'POST'])
@login_required
def new_student():
    form = NewStudentForm()
    if form.validate_on_submit():
        student = Student(id=form.id.data, last_name=form.last_name.data, first_name=form.first_name.data, class_year=form.class_year.data, email=form.email.data)
        db.session.add(student)
        db.session.commit()
        db.session.close()
        return redirect(url_for('index'))
    return render_template('new_student.html', title='New Student', form=form)