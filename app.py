from flask import Flask, render_template
from flask_login import LoginManager, current_user
from profiles.routes import profile_bp
from todo.routes import task_bp
from database.enjine import db
from auth.routes import auth_bp
from database.models.auth import User


app = Flask(__name__)
login_manager = LoginManager()


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SECRET_KEY'] = 'nfoe94gk349ungwgweli3kmf'

db.init_app(app)
login_manager.init_app(app)

login_manager.login_view = 'auth.login'

with app.app_context():
    db.create_all()

app.register_blueprint(task_bp, url_prefix='/tasks')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(profile_bp, url_prefix='/profile')


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()


@app.route('/')
def main():
    return render_template('start.html', current_user=current_user)
# Если функция начинается с is - значит использует Boolen-знчения

if __name__ == '__main__':
    app.run(debug=True)