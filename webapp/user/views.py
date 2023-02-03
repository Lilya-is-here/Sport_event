from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import logout_user
from flask_security import login_required, LoginForm, RegisterForm
from webapp.model import db, UserBet


blueprint = Blueprint('user_blueprint', __name__, url_prefix='/users')


@blueprint.route('/login')
def login():
    form = LoginForm()
    return render_template(
        'security/login_user.html', login_user_form=form
        )


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы успешно разлогинились')
    return redirect(url_for('index'))


@blueprint.route('/register')
def register():
    form = RegisterForm()
    return render_template(
        'security/register_user.html', register_user_form=form
        )


@blueprint.route('/profile')
@login_required
def profile():
    title = "Sport event"
    headline = "Profile"
    bet = db.session.query(UserBet).all()
    return render_template("user/profile.html", title=title, headline=headline, bet=bet)
