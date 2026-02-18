from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required
from app.persistence.audience_type_repository import AudienceTypeRepository

api = Namespace('audience_types', description='Audience types operations')


@api.route('/')
class AudienceTypes(Resource):
    @jwt_required()
    @api.response(200, 'OK')
    def get(self):
        audienceT_repo = AudienceTypeRepository()
        return [element.to_dict() for element in audienceT_repo.get_all()], 200
