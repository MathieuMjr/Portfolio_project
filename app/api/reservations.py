from flask_restx import Namespace, Resource
from app.services import res_service
from flask_jwt_extended import (jwt_required,
                                get_jwt,
                                get_jwt_identity)
from pydantic import ValidationError
from app.services.errors import (UniqueContraintError,
                                 ThemeDontMatchResType,
                                 DeactivatedResourceError)
from app.persistence.user_repository import UserRepository
from app.services.utils import check_id
from flask import request
from datetime import datetime

api = Namespace('reservations', description='Reservations operations')


@api.route('/')
class Reservations(Resource):
    @jwt_required()
    def post(self):
        # fetch data
        data = api.payload

        # extract and check token claims and authorizations
        identity = get_jwt_identity()
        claims = get_jwt()
        role = claims['role']
        user_res_types = claims['reservation_types']

        if not (role or data['reservation_type_id'] in user_res_types):
            return {'error': 'Unauthorized action'}, 403

        # add identity to data
        if role is True and 'author_id' in data:
            user_repo = UserRepository()
            check_id('User', data['author_id'], user_repo)
        else:
            data['author_id'] = identity

        # create reservation
        try:
            return res_service.create_reservation(data)
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
        except ThemeDontMatchResType as e:
            return {'error': str(e)}, 400
        except (LookupError, DeactivatedResourceError) as e:
            return {'error': str(e)}, 404


@api.route('/me/reservations')
class UserReservations(Resource):
    @jwt_required()
    def get(self):
        identity = get_jwt_identity()
        start = request.args.get('from')
        end = request.args.get('to')

        if not start or not end:
            return {'error': "from date and to date are missing"}, 400

        if start > end:
            return {'error': "from value must be before to value"}, 400

        start_date = datetime.strptime(start, "%Y-%m-%d").date()
        end_date = datetime.strptime(end, "%Y-%m-%d").date()
        try:
            return res_service.user_reservations(
                identity, start_date, end_date)
        except (LookupError, DeactivatedResourceError) as e:
            return {'error': str(e)}, 404


@api.route('/<reservation_id>')
class ReservationId(Resource):
    @jwt_required()
    def get(self, reservation_id):
        identity = get_jwt_identity()
        claims = get_jwt()
        role = claims['role']
        try:
            res = res_service.get_by_id(reservation_id)
            if not role and identity != res.author_id:
                return {'error': 'Unauthorized action'}, 403
            return res.to_dict()
        except LookupError as e:
            return {'error': str(e)}, 404
