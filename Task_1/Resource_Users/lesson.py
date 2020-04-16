from flask import Flask, render_template, abort
from Task_1.Resource_Users import users_resource
from Task_1.data_models.users import User
from Task_1.data_models import db_session
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def main():
    return render_template("test.html")


def abort_if_users_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    print(user)
    if not user:
        abort(404, message=f"User {user_id} not found")


if __name__ == "__main__":
    db_session.global_init("../db/program.sqlite")
    api.add_resource(users_resource.UsersListResource, '/api/users')
    api.add_resource(users_resource.UsersResource, '/api/users/<int:user_id>')
    app.run(port=5001, host='127.0.0.1')
