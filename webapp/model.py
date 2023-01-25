from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)



class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    sport = db.Column(db.String, nullable=False)
    time = db.Column(db.DateTime, nullable=True, default=datetime.now())
    result = db.Column(db.String, nullable=False)
    coefficient = db.relationship('Coefficient', backref='event')

    def __repr__(self):
        return "<Event {} {}>".format(
            self.name, self.time)


class Coefficient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(
        db.Integer, db.ForeignKey('event.id'), nullable=False)
    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable=False)
    BK = db.Column(db.String, nullable=False)
    Result = db.Column(db.String, nullable=False)
    coefficient = db.Column(db.String, nullable=False)
    user_bets = db.relationship('UserBet', backref='coefficient')

    def __repr__(self):
        return "<Results {} {}>".format(
            self.BK, self.coefficient)


class UserBet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_bet = db.Column(db.Integer, nullable=False)
    coefficient_id = db.Column(
        db.Integer, db.ForeignKey('coefficient.id'), nullable=False)
    user_id = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return "<Results {} {}>".format(
            self.user_id, self.user_bet)
