from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# Flask-SqlAlchemy = это штука которая позваоляет Python-кодом выполнять SQL-команды
#Flask-Form

class RegistretionForm(FlaskForm):
    username = StringField('Никнейм', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=3, max=8)])
    config_password = PasswordField('Подтвердите пароль', validators=[
        DataRequired(),
        EqualTo('password', message='Пароль не совпадает')
    ])
    submit = SubmitField('Зарегистрироваться')