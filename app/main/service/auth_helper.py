from app.main.model.auctions_user import Auctions_user
from ..service.blacklist_service import save_token
from typing import Dict, Tuple


class Auth:

    @staticmethod
    def login_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        try:
            # fetch the user data
            user = Auctions_user.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                auth_token = Auctions_user.encode_auth_token(user.id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_user(data: str) -> Tuple[Dict[str, str], int]:
        if data:
            auth_token = data.split(" ")[0]
        else:
            auth_token = ''
        if auth_token:
            resp = Auctions_user.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = Auctions_user.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = Auctions_user.query.filter_by(id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'id': user.id,
                        'email': user.email,
                        'is_active': str(user.is_active),
                        'date_joined': str(user.date_joined)
                    }
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401
