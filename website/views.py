from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from .models import Note
from . import db
import json

# Function: Blueprint
# Purpose: Create a Blueprint instance for organizing related routes.
# Description: Blueprints help to organize and group routes in a Flask application.
#              This Blueprint is named "views" and is used to register routes related 
#              to the application's views.
# Returns: A Blueprint instance.

views = Blueprint("views", __name__)

# Function: home
# Purpose: Render the home page.
# Description: This route renders the home page template and passes the current user 
#              to the template for context.
# Returns: Renders the "home.html" template.

@views.route("/", )
@views.route("/home", )
def home():
    return render_template("home.html", user=current_user)

# Function: notes
# Purpose: Handle displaying and adding notes.
# Description: This route handles GET and POST requests. On GET request, it renders 
#              the "notes.html" template. On POST request, it processes form data to 
#              add a new note to the database if the note is valid.
# Returns: Renders the "notes.html" template on GET request, and processes the form data 
#          and adds a new note on POST request.

@views.route("/notes", methods=['GET', 'POST'])
def notes():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added:', category='success')

    return render_template("notes.html", user=current_user)

# Function: delete_note
# Purpose: Handle deleting a note.
# Description: This route handles POST requests to delete a note. It receives note data 
#              in JSON format, retrieves the note from the database, and deletes it if the 
#              current user is the owner.
# Returns: A JSON response indicating the deletion status.

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

# Class: Note
# Description: This represents a database model for storing notes.
# Details: The Note class likely has fields for the note's data and the user ID of the owner.
# Relationship: Instances of the Note class are used in the notes and delete_note functions 
#               to interact with the database.
