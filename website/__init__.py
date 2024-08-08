from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Initialize the SQLAlchemy object
db = SQLAlchemy()
# Define the name of the database file
DB_NAME = "database.db"

# Function: create_app
# Purpose: Factory function to create and configure the Flask application instance.
# Description: This function sets up the Flask application by configuring settings, 
#              initializing extensions, and registering blueprints. It ensures the 
#              application is created with all necessary components for running a web service.
# Returns: A Flask application instance configured and ready to be run.

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'  # Secret key for session management and CSRF protection
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'  # URI for the SQLite database
    db.init_app(app)  # Initialize the database with the app

    # Import and register blueprints for views and authentication routes
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Import models to ensure they are registered with SQLAlchemy
    from .models import User, Note

    # Create database tables within the application context
    with app.app_context():
        db.create_all()

    # Initialize the login manager for user session management
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'  # Set the default login view
    login_manager.init_app(app)

    # User loader function for the login manager
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))  # Load the user by ID

    return app  # Return the configured app instance

# Function: create_database
# Purpose:
