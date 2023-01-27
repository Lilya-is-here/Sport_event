from flask import Flask, render_template
from flask_admin import Admin

from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mailman import Mail

from flask_security import Security, user_registered
from webapp.admin import HomeAdminView, AdminView
import logging

from webapp.user.views import blueprint as user_blueprint

from webapp.model import db, Coefficient, Event, UserBet
from webapp.user.models import User, user_datastore


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
    admin.add_view(AdminView(UserBet, db.session))

    security = Security(app, user_datastore)

    # Добавление роли к пользователю по дефолту
    @user_registered.connect_via(app)
    def user_registered_sighandler(sender, **extra):
        logging.getLogger(__name__).debug("register handler: %s", extra)
        user = extra.get("user")
        user_datastore.add_role_to_user(user, "user")
        user_datastore.commit()

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
