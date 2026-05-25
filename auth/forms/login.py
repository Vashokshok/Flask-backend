from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# Flask-SqlAlchemy = это штука которая позваоляет Python-кодом выполнять SQL-команды
#Flask-Form

class LoginForm(FlaskForm):
    email = StringField('Почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=3, max=8)])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')