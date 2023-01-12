from flask import Flask, render_template, redirect, url_for, request
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
from flask_migrate import Migrate

from flask_security import Security, current_user
from webapp.user.views import blueprint as user_blueprint

from webapp.model import db, Coefficient, Event
from webapp.user.models import User, user_datastore


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    migrate = Migrate(app, db)

    class AdminView(ModelView):
        def is_accessible(self):
            return current_user.has_role('admin')

        def inaccessible_callback(self, name):
            return redirect(url_for(security.login, next=request.url))

    class HomeAdminView(AdminIndexView):
        def is_accessible(self):
            return current_user.has_role('admin')

        def inaccessible_callback(self, name):
            return redirect(url_for(security.login, next=request.url))

    admin = Admin(app, 'FlaskApp', url='/',
                  index_view=HomeAdminView(name='Home'))
    admin.add_view(AdminView(User, db.session))
    admin.add_view(AdminView(Event, db.session))
    admin.add_view(AdminView(Coefficient, db.session))

    security = Security(app, user_datastore)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        title = "Sport event"
        headline = "Hello Sport"
        events = db.session.query(Event,
                                  Coefficient).filter(
                                                      Event.id == Coefficient.event_id).all()
        return render_template(
            "main_page/index.html",
            title=title,
            headline=headline,
            events=events
            )
    return app
