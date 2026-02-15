from flask_restx import Namespace, Resource
from flask_jwt_extended import (jwt_required)
from app.persistence.structure_type_repository import StructureTypeRepository

api = Namespace('struct_types', description='Structure types operations')


@api.route('/')
class StructTypes(Resource):
    @jwt_required()
    def get(self):
        strucT_repo = StructureTypeRepository()
        return [element.to_dict() for element in strucT_repo.get_all()]
