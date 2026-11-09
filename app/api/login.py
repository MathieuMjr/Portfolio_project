from flask_restx import Namespace, Resource
from app.services import user_service
from flask_jwt_extended import create_access_token, set_access_cookies
from flask import make_response

api = Namespace('login', description='Login route and token creation')


@api.route('/')
class Login(Resource):
    def post(self):
        data = api.payload
        user = user_service.user_repo.get_by_attribute('email', data['email'])
        if len(user) == 0 or user[0].is_active is False:
            return {'error': 'Invalid credentials'}, 401
        else:
            res_types_ids = [
                element.id for element in user[0].reservation_types]
            if user[0].verify_pwd(data['password']):
                access_token = create_access_token(
                    identity=user[0].id,
                    additional_claims={
                        'role': user[0].role,
                        'reservation_types': res_types_ids
                    }
                )
                response = make_response({'message': "success"}, 200)
                set_access_cookies(response, access_token)
                return response
            else:
                return {'error': 'Invalid credentials'}, 401
