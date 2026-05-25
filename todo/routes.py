from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required

from database.models.todo import Task
from database.enjine import db


task_bp = Blueprint('tasks', __name__, template_folder='templates')


@task_bp.route('/')
@login_required# <---!!!!! это чтобы не авторизованный пользователь
#не смог зайти на страницу с задачами.
# можно указывать там где ты не хочешь чтобы не авторизованные не смогли зайти на страницу
def get_all_tasks():
    all_tasks = Task.query.all() # Берем все данные с базы данных
    return render_template('all_tasks.html', tasks_db=all_tasks)


# Статик - стоит
# Демонически - движется
@task_bp.route('/read/<int:id>')
@login_required
def task_detail(id):
    task_one = Task.query.filter_by(id=id).first()
    return render_template('index.html', task_one=task_one)

@task_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_task():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        # tasks_db.append({'id': len(tasks_db) + 1, 'title': title, 'description': description})
        task = Task(title=title, description=description)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('tasks.get_all_tasks'))
    return render_template('add_task.html')

@task_bp.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_tasks(id):
    tasks = Task.query.filter_by(id=id).first()
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        if title:
            tasks.title = title
        if description:
            tasks.description = description
        db.session.commit()
    return render_template('update.html', task_one=tasks)


@task_bp.route('/delate/<int:id>', methods=['POST'])
@login_required
def delate_task(id):
    tasks = Task.query.filter_by(id=id).first()
    db.session.delete(tasks)
    db.session.commit()
    return redirect(url_for('tasks.get_all_tasks'))


# html чтобы возврашалось ДЗ
# от 400 - 499 - связано с клиентом
# от 500 - 599 - связано с сервером
# render_template() — отобразить шаблон
# POST - запрос
# redirect - перенаправление
# ДЗ - сделать так чтобы задачи достовались с Базы данных