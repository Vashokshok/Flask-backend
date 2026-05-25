from flask import Blueprint, render_template, redirect, url_for
from auth.forms.register import RegistretionForm
from flask_login import login_user, logout_user
from auth.forms.login import LoginForm
from database.models.auth import User
from database.enjine import db

auth_bp = Blueprint('auth', __name__, template_folder='templates')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            print('все правильно')
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main'))
        else:
            print('Неправильный логин или пароль')
    return render_template('login.html', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])  # ← добавлен POST
def register():
    form = RegistretionForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main'))
    return render_template('register.html', form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main'))