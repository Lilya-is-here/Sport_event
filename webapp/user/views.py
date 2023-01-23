from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user
from flask_security import login_required, LoginForm, RegisterForm
from datetime import datetime

from webapp.user.models import User, user_datastore
from webapp.model import db

blueprint = Blueprint('user_blueprint', __name__, url_prefix='/users')


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = 'Авторизация'
    login_form = LoginForm()
    return render_template(
        'security/login_user.html', page_title=title, login_user_form=login_form
        )


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(
            User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы успешно вошли на сайт')
            return redirect(url_for('index'))

    flash('Неправильные имя или пароль')
    return redirect(url_for('user_blueprint.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы успешно разлогинились')
    return redirect(url_for('index'))


@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = 'Регистрация'
    form = RegisterForm()
    return render_template(
        'security/register_user.html', page_title=title, register_user_form=form
        )


@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegisterForm()
    if form.validate_on_submit():
        user_datastore.create_user(
                                   username=form.username.data,
                                   mail=form.email.data,
                                   role='user',
                                   password=form.email.data,
                                   confirmed_at=datetime.datetime.now())
        db.session.commit()
        
        flash('Вы успешно зарегистрировались')
        return redirect(url_for('user_blueprint.login'))
    # else:
    #     for field, errors in form.errors.items():
    #         for error in errors:
    #             flash('Ошибка в поле {} : {}'.format(
    #                 getattr(form, field).label.text, error
    #                 ))
    #     return redirect(url_for('user_blueprint.register'))

@blueprint.route('/profile')
@login_required
def profile():
    title = "Sport event"
    headline = "Profile"
    return render_template("user/profile.html", title=title, headline=headline)
