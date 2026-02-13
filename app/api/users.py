from flask_restx import Resource, Namespace
from flask_jwt_extended import (get_jwt, jwt_required)
from app.services import user_service
from pydantic import ValidationError

api = Namespace('users', description='User operations')


@api.route('/')
class Users(Resource):
    @jwt_required()
    def post(self):
        data = api.payload
        claims = get_jwt()
        if not claims['is_admin']:
            return {'error': 'Priviledge authorizations required'}, 403
        try:
            response = user_service.create_user(data)
            return response, 201
        except ValidationError as e:
            errors = []
            for element in e.errors():
                errors.append({
                    'field': element['loc'][0],
                    'value': element['input'],
                    'msg': element['msg']})
            return {'error': errors}, 400
        except LookupError as e:
            return {'error': str(e)}, 404
        except ValueError as e:
            return {'error': str(e)}, 400

    def get(self):
        pass


@api.route('/<user_id>')
class UserIds(Resource):
    def get(self):
        pass

    def update(self):
        pass

    @jwt_required()
    def delete(self):
        pass
