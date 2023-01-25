from flask_security import UserMixin, RoleMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_security import SQLAlchemyUserDatastore


from webapp.model import db



roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer,
                                 db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer,
                                 db.ForeignKey('role.id'))
                       )


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(50), unique=True, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    coefficient = db.relationship('Coefficient', backref='user', lazy=True)
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users'))
    user_bets = db.relationship('UserBet', backref='user')


    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return '<User name={} id={}>'.format(self.username, self.id)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)


# Flask-Security

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
