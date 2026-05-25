from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from database.models.auth import User
from database.enjine import db



profile_bp = Blueprint('profile', __name__, template_folder='templates')


@profile_bp.route('/')
@login_required
def profile():
    if current_user.is_authenticated:
        return render_template('profile.html', current_user=current_user)
    return None



@profile_bp.route('/change_username', methods=['GET', 'POST'])
@login_required
def change_username():
    if request.method == 'POST':
        username = request.form.get('new-username')
        email = request.form.get('new-email')
        older_pass = request.form.get('old-password')
        new_pass = request.form.get('new-password')
        print(username)
        if username and len(username) >= 3:
            current_user.username = username
        if email:
            current_user.email = email
        if older_pass and not current_user.check_password(older_pass):
            return render_template('change_username.html', error="Старый пароль неверный")
        if new_pass and len(new_pass) >= 6:
            current_user.set_password(new_pass)
        db.session.commit()
        return redirect(url_for('profile.profile'))

    return render_template('change_username.html')




# Для смены почты, пароль - сначало старый потом новый , если не правильно то снова чтобы ввел

# git add .
# git status
# git commit -m " "
# git push
