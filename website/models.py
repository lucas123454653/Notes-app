from . import db
from flask_login import UserMixin



class Note(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    
    


class User(db.model, UserMixin):
    id = db.Column(db.Interger, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.string(150))
    notes = db.relationship('Note')