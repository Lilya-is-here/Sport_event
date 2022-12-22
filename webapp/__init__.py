from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from webapp.user.views import blueprint as user_blueprint
from webapp.admin.views import blueprint as admin_blueprint

from webapp.model import db
from webapp.user.models import User


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    migrate = Migrate(app, db)

    @app.route('/')
    def index():
        title = "Sport event"
        headline = "Hello Sport"
        return render_template("main_page/index.html", title=title, headline=headline)

    return app
