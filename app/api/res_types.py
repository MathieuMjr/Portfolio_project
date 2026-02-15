from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required
from app.persistence.theme_repository import ThemeRepository
from app.persistence.reservation_type_repository import (
    ReservationTypeRepository)
from app.services.utils import check_id
from app.services.errors import DeactivatedResourceError

api = Namespace(
    'reservation_types', description='Reservation types operations')


@api.route('/')
class ResTypes(Resource):
    @jwt_required()
    def get(self):
        resType_repo = ReservationTypeRepository()
        return [element.to_dict() for element in resType_repo.get_all()]


@api.route('/<reservation_type_id>/themes')
class Themes(Resource):
    @jwt_required()
    def get(self, reservation_type_id):
        resT_repo = ReservationTypeRepository()
        theme_repo = ThemeRepository()
        try:
            check_id('Reservation type', reservation_type_id, resT_repo)
            return [
                element.to_dict() for element in theme_repo.get_by_attribute(
                    'reservation_type_id', reservation_type_id)]
        except (LookupError, DeactivatedResourceError) as e:
            return {'error': str(e)}, 404
