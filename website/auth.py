from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

# Function: Blueprint
# Purpose: Create a Blueprint instance for organizing authentication-related routes.
# Description: Blueprints help to organize and group routes in a Flask application.
#              This Blueprint is named 'auth' and is used to register routes related to authentication.
# Returns: A Blueprint instance.

auth = Blueprint('auth', __name__)

# Function: login
# Purpose: Handle user login.
# Description: This route handles GET and POST requests. On GET request, it renders the login page. 
#              On POST request, it verifies user credentials and logs in the user if valid.
# Returns: Renders the "login.html" template on GET request, and redirects to the home page on successful login.

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

# Function: logout
# Purpose: Handle user logout.
# Description: This route logs out the current user.
# Returns: Redirects to the login page after logging out.

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# Function: sign_up
# Purpose: Handle user sign-up.
# Description: This route handles GET and POST requests. On GET request, it renders the sign-up page. 
#              On POST request, it processes form data to create a new user account if the input is valid.
# Returns: Renders the "signup.html" template on GET request, and redirects to the home page on successful sign-up.

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)

# Class: User
# Description: This represents a database model for storing user information.
# Details: The User class likely has fields for the user's ID, email, hashed password, first name, and notes.
# Relationship: Instances of the User class are used in the login, logout, and sign-up functions 
#               to interact with the database.
