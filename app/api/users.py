from flask_restx import Resource, Namespace
from flask_jwt_extended import (get_jwt, jwt_required, get_jwt_identity)
from app.services import user_service
from pydantic import ValidationError
from app.services.errors import (UniqueContraintError,
                                 DeactivatedResourceError)
from app.validators.users import UserPayload, SelfUpdate, UpdateUserAsAdmin

api = Namespace('users', description='User operations')

# Models for swagger documentation imported from Pydantics
user_payload = api.schema_model(
    'User paylaod', UserPayload.model_json_schema())
self_update = api.schema_model(
    'Self update', SelfUpdate.model_json_schema())
update_as_admin = api.schema_model(
    'Update as admin', UpdateUserAsAdmin.model_json_schema()
)


@api.route('/')
class Users(Resource):
    @jwt_required()
    @api.response(201, 'Created')
    @api.response(400, 'Invalid input')
    @api.response(404, 'Resource not found')
    @api.response(409, 'Unique constraint violation')
    @api.expect(user_payload, validate=False)
    def post(self):
        data = api.payload
        claims = get_jwt()
        if not claims['role']:
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
        except (LookupError, DeactivatedResourceError) as e:
            return {'error': str(e)}, 404
        except UniqueContraintError as e:
            return {'error': str(e)}, 409

    @jwt_required()
    def get(self):
        claims = get_jwt()
        if not claims['role']:
            return {'error': 'Priviledge authorizations required'}, 403
        return [element.to_dict() for element in user_service.get_all()]


@api.route('/me')
class UserUpdate(Resource):
    @jwt_required()
    def get(self):
        identity = get_jwt_identity()
        claims = get_jwt()
        try:
            return user_service.get_identity(identity, claims)
        except (LookupError, DeactivatedResourceError) as e:
            return {'error': str(e)}, 404

    @jwt_required()
    @api.response(200, 'Password updated successfully')
    @api.response(400, 'Invalid input')
    @api.response(404, 'Resource not found or deactivated')
    @api.expect(self_update, validate=False)
    def put(self):
        data = api.payload
        identity = get_jwt_identity()
        try:
            user_service.self_update(identity, data)
            return {'message': 'Password updated successfully'}, 204
        except ValidationError as e:
            errors = []
            for element in e.errors():
                errors.append({
                    'field': element['loc'][0],
                    'value': element['input'],
                    'msg': element['msg']})
            return {'error': errors}, 400
        except (LookupError, DeactivatedResourceError) as e:
            return {'error': str(e)}, 404


@api.route('/<user_id>')
class UserIds(Resource):
    @jwt_required()
    @api.response(200, 'OK')
    @api.response(403, 'Priviledge required')
    @api.response(404, 'Resource not found')
    def get(self, user_id):
        identity = get_jwt_identity()
        claims = get_jwt()
        role = claims['role']
        if not role and identity != user_id:
            return {'error': 'Unauthorized action'}, 403
        try:
            return user_service.get_by_id(user_id), 200
        except LookupError as e:
            return {'error': str(e)}, 404

    @jwt_required()
    @api.response(204, 'OK')
    @api.response(403, 'Priviledge required')
    @api.response(404, 'Resource not found')
    @api.response(409, 'Unique constrainte violation')
    @api.doc(description="All fields are optional")
    @api.expect(update_as_admin, validate=False)
    def patch(self, user_id):
        data = api.payload
        claims = get_jwt()
        role = claims['role']
        if not role:
            return {'error': 'Unauthorized action'}, 403
        try:
            user_service.patch(user_id, data)
            return {'message': 'User successfully udpated'}, 204
        except ValidationError as e:
            errors = []
            for element in e.errors():
                errors.append({
                    'field': element['loc'][0],
                    'value': element['input'],
                    'msg': element['msg']})
            return {'error': errors}, 400
        except UniqueContraintError as e:
            return {'error': str(e)}, 409
        except (LookupError, DeactivatedResourceError) as e:
            return {'error': str(e)}, 404

    @jwt_required()
    @api.response(204, 'User successfully deactivated')
    @api.response(403, 'Priviledge required')
    @api.response(404, 'Resource not found')
    def delete(self, user_id):
        claims = get_jwt()
        role = claims['role']
        if not role:
            return {'error': 'Unauthorized action'}, 403
        try:
            user_service.delete(user_id)
            return {'message': 'User successfully deactivated'}, 204
        except LookupError as e:
            return {'error': str(e)}, 404
