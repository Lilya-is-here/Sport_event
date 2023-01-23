from flask import Flask, render_template
from flask_admin import Admin

from flask_login import LoginManager
from flask_migrate import Migrate
from webapp.admin import HomeAdminView, AdminView

from flask_security import Security
from webapp.user.views import blueprint as user_blueprint

from webapp.model import db, Coefficient, Event, User_bet
from webapp.user.models import User, user_datastore
from flask_mail import Mail


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    mail = Mail(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    migrate = Migrate(app, db)

    admin = Admin(app, 'FlaskApp', url='/',
                  index_view=HomeAdminView(name='Home'))
    admin.add_view(AdminView(User, db.session))
    admin.add_view(AdminView(Event, db.session))
    admin.add_view(AdminView(Coefficient, db.session))
    admin.add_view(AdminView(User_bet, db.session))

    security = Security(app, user_datastore)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        title = "Sport event"
        headline = "Hello Sport"
        events = db.session.query(Event).all()

        return render_template(
            "main_page/index.html",
            title=title,
            headline=headline,
            events=events,
            )
    return app
