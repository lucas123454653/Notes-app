from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Class: Note
# Description: This class represents the Note model, which corresponds to the notes table in the database.
# Details: Each note has an ID, data content, a timestamp for the date created, and a reference to the user who created it.
# Relationship: A Note is associated with a User via the user_id foreign key.

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each note
    data = db.Column(db.String(10000))  # Content of the note
    date = db.Column(db.DateTime(timezone=True), default=func.now())  # Timestamp of when the note was created, defaults to current time
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Foreign key linking to the User who created the note

# Class: User
# Description: This class represents the User model, which corresponds to the users table in the database.
# Details: Each user has an ID, email, password, first name, and a list of notes they have created.
# Relationship: A User can have multiple notes, established via the relationship to the Note class.

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each user
    email = db.Column(db.String(150), unique=True)  # Email of the user, must be unique
    password = db.Column(db.String(150))  # Password of the user
    first_name = db.Column(db.String(150))  # First name of the user
    notes = db.relationship('Note')  # Relationship indicating that a user can have multiple notes
