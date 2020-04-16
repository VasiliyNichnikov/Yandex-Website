from flask import jsonify
import datetime
from flask_restful import Resource
from flask_restful import reqparse
from flask import abort, app
from Task_1.data_models import db_session
from Task_1.data_models.jobs import Jobs


def abort_if_users_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found")


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_users_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        return jsonify(
            {
                'job': job.to_dict(only=('id',
                                         'team_leader',
                                         'job',
                                         'work_size',
                                         'collaborators',
                                         'start_date',
                                         'end_date',
                                         'is_finished'))
            }
        )

    def delete(self, job_id):
        abort_if_users_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success:': 'OK'})


class JobsListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('team_leader', required=True)
    parser.add_argument('job', required=True)
    parser.add_argument('work_size', required=True)
    parser.add_argument('collaborators', required=True)
    parser.add_argument('start_date', required=True)
    parser.add_argument('end_date', required=True)
    parser.add_argument('is_finished', required=True)

    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({
            'jobs': [job.to_dict(only=('id',
                                       'team_leader',
                                       'job',
                                       'work_size',
                                       'collaborators',
                                       'start_date',
                                       'end_date',
                                       'is_finished')) for job in jobs]
        })

    def post(self):
        args = self.parser.parse_args()
        session = db_session.create_session()
        jobs = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date=datetime.datetime.now(),
            end_date=datetime.datetime.now(),
            is_finished=bool(args['is_finished'])
        )
        session.add(jobs)
        session.commit()
        return jsonify({'success': 'OK'})