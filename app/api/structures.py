from flask_restx import Namespace, Resource
from flask_jwt_extended import (jwt_required)
from flask import request
from app.services import structure_service
from pydantic import ValidationError
from app.services.errors import (UniqueContraintError,
                                 DeactivatedResourceError)
from app.validators.structure import StructurePaylaod

api = Namespace('structures', description='Structures operations')

# Pydantic schemas for swagger doc
structure_payload = api.schema_model(
    'Structure payload', StructurePaylaod.model_json_schema())


@api.route('/')
class Structures(Resource):
    @jwt_required()
    @api.response(201, "Created")
    @api.response(400, 'Invalid input')
    @api.response(401, 'Authentication needed')
    @api.response(404, 'Resource not found or deactivated')
    @api.response(409, 'Unique constraint violation')
    @api.expect(structure_payload, validate=False)
    def post(self):
        data = api.payload
        try:
            return structure_service.create_struct(data), 201
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
        structT_id = request.args.get("type_id")
        print(structT_id)
        zip_code = request.args.get('zip')
        print(zip_code)

        if not structT_id or not zip_code:
            return {'error': 'A query parameter is missing'}, 400

        try:
            return structure_service.get_struct_id_zip(structT_id, zip_code)
        except (LookupError, DeactivatedResourceError) as e:
            return {'error': str(e)}, 404
        except (ValueError) as e:
            return {'error': str(e)}, 400
