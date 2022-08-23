from .. import flask_bcrypt
from datetime import datetime
from app.main import db
from app.main.model.auctions_user import Auctions_user
from typing import Dict, Tuple


def save_new_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    user = Auctions_user.query.filter_by(email=data['email']).first()
    if not user:
        new_user = Auctions_user(
            password=flask_bcrypt.generate_password_hash(data['password']).decode('utf-8'),
            # last_login=null,
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            is_staff=False,
            is_active=True,
            date_joined=datetime.now()
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return Auctions_user.query.all()


def get_a_user(id):
    return Auctions_user.query.filter_by(id=id).first()


def generate_token(user: Auctions_user) -> Tuple[Dict[str, str], int]:
    try:
        # generate the auth token
        auth_token = Auctions_user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data: Auctions_user) -> None:
    db.session.add(data)
    db.session.commit()

