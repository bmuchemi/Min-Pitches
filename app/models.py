from datetime import timezone
from . import db
from flask_login import  UserMixin
from sqlalchemy.sql import func

class Pitches(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255))
    text = db.Column(db.String(10000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'));
    posted = db.Column(db.DateTime(timezone=True),default=func.now())
    comments = db.relationship('Comments', backref='pitches', lazy='dynamic')


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    comment = db.Column(db.String(10000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    pitches = db.relationship('Pitches', backref='user', lazy='dynamic')
    comments = db.relationship('Comments', backref='comments', lazy='dynamic')
    about = db.Column(db.String(255))
    avatar = db.Column(db.String())