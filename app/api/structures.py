from flask_restx import Namespace, Resource
from flask_jwt_extended import (jwt_required)
from app.services import structure_service
from pydantic import ValidationError
from app.services.errors import (UniqueContraintError,
                                 DeactivatedResourceError)

api = Namespace('structures', description='Structures operations')


@api.route('/')
class Structures(Resource):
    @jwt_required()
    def post(self):
        data = api.payload
        try:
            return structure_service.create_struct(data)
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
