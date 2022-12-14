from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


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
