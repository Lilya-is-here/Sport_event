from datetime import datetime
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    sport = db.Column(db.String, nullable=False)
    time = db.Column(db.DateTime, nullable=True, default=datetime.now())
    result = db.Column(db.String, nullable=False)
    coefficient = db.relationship('Coefficient', backref='event', lazy=True)

    def __repr__(self):
        return "<Event {} {}>".format(
            self.name, self.datetime)


class Coefficient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(
        db.Integer, db.ForeignKey('event.id'), nullable=False)
    BK = db.Column(db.String, nullable=False)
    Result = db.Column(db.String, nullable=False)
    coefficient = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Results {} {}>".format(
            self.BK, self.coefficient)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)
    email = db.Column(db.String(50))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return '<User name={} id={}>'.format(self.username, self.id)
