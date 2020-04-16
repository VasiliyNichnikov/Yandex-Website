from flask_login import LoginManager
from flask_login import logout_user
from flask_login import login_user
from flask import redirect
from flask import Flask
from flask import abort
from Task_1.Resource_Users import users_resource
from Task_1.Resourse_Jobs import jobs_resource
from Task_1.data_models import db_session
from Task_1.data_models.users import User
from Task_1.data_models.jobs import Jobs
from Task_1.FormLogin import LoginForm
from Task_1.FormWorks import WorksForm
from Task_1.FormRegister import RegisterForm
from flask import render_template
from flask_restful import Api


app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(User).get(user_id)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/')
        return render_template('login.html', message="Неправильный логин или пароль", form=form)
    return render_template('login.html', title="Авторизация", form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.repeat_password.data:
            return render_template('register.html', title="Решистрация", form=form,
                                   message="Пароли не совпадают")
        session = db_session.create_session()
        if session.query(User).filter(User.email == form.login_email.data).first():
            return render_template('register.html', title="Регистрация", form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.specialty.data,
            address=form.address.data,
            hashed_password=form.password,
            email=form.login_email.data)
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/')
def works():
    session = db_session.create_session()
    all_jobs = session.query(Jobs).all()
    list_jobs = []
    for i in all_jobs:
        list_jobs.append({"id": i.id,
                          "team_leader": i.team_leader,
                          "job": i.job,
                          "work_size": i.work_size,
                          "collaborators": i.collaborators,
                          "start_date": i.start_date,
                          "end_date": i.end_date,
                          "is_finished": i.is_finished
                          })
    return render_template("work_log.html", title="Журнал работ", listUsers=list_jobs)


@app.route('/add_works', methods=['GET', 'POST'])
def add_works():
    form = WorksForm()

    if form.validate_on_submit():
        session = db_session.create_session()
        job = Jobs(
            team_leader=form.team_leader.data,
            job=form.job.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            is_finished=form.is_finished.data
        )
        session.add(job)
        session.commit()
        return redirect('/')
    return render_template("add_works.html", title="Добавление работ", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


if __name__ == "__main__":
    db_session.global_init("db/program.sqlite")
    api.add_resource(users_resource.UsersListResource, '/api/users')
    api.add_resource(users_resource.UsersResource, '/api/users/<int:user_id>')

    api.add_resource(jobs_resource.JobsListResource, '/api/jobs')
    api.add_resource(jobs_resource.JobsResource, '/api/jobs/<int:job_id>')
    app.run(port=5001, host='127.0.0.1')
