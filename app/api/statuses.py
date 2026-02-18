from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required
from app.persistence.status_repository import StatusRepository

api = Namespace('statuses', description='Statuses operations')


@api.route('/')
class Statuses(Resource):
    @jwt_required()
    @api.response(200, 'OK')
    def get(self):
        status_repo = StatusRepository()
        return [element.to_dict() for element in status_repo.get_all()], 200
