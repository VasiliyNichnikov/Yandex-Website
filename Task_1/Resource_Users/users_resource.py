from flask import jsonify
import datetime
from flask_restful import Resource
from flask_restful import reqparse
from Task_1.model_user_authorization_form import abort_if_users_not_found
from Task_1.data_models import db_session
from Task_1.data_models.users import User


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_users_not_found()
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify(
            {
                'user': user.to_dict(only=('id',
                                           'surname',
                                           'name',
                                           'age',
                                           'position',
                                           'speciality',
                                           'address',
                                           'email',
                                           'hashed_password',
                                           'modified_date'))
            }
        )

    def delete(self, user_id):
        abort_if_users_not_found()
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success:': 'OK'})


class UsersListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('surname', required=True)
    parser.add_argument('name', required=True)
    parser.add_argument('age', required=True)
    parser.add_argument('position', required=True)
    parser.add_argument('speciality', required=True)
    parser.add_argument('address', required=True)
    parser.add_argument('email', required=True)
    parser.add_argument('hashed_password', required=True)
    parser.add_argument('modified_date', required=True)

    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({
            'users': [user.to_dict(only=('id',
                                         'surname',
                                         'name',
                                         'age',
                                         'position',
                                         'speciality',
                                         'address',
                                         'email',
                                         'hashed_password',
                                         'modified_date')) for user in users]
        })

    def post(self):
        args = self.parser.parse_args()
        session = db_session.create_session()
        users = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            hashed_password=args['hashed_password'],
            modified_date=datetime.datetime.now()
        )
        session.add(users)
        session.commit()
        return jsonify({'success': 'OK'})