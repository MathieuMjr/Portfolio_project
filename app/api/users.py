from flask_restx import Resource, Namespace
# from flask_jwt_extended import get_jwt_identity,
# create_access_token,
# jwt_required
from app.services import user_service
from pydantic import ValidationError

api = Namespace('users', description='User operations')


@api.route('/')
class Users(Resource):
    def post(self):
        data = api.payload
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
            return {'error': e}, 400
