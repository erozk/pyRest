
from .. import db, flask_bcrypt
import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt
from typing import Union

class Auctions_user(db.Model):
    """ auction user model for storing user related details """
    __tablename__ = "auctions_user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    password = db.Column(db.String(128), nullable=False)
    last_login = db.Column(db.DateTime)
    is_superuser = db.Column(db.Boolean, nullable=False, default=False)
    username = db.Column(db.String(150), unique=True, nullable =False)
    first_name = db.Column(db.String(150), nullable =False)
    last_name= db.Column(db.String(150), nullable =False)
    email = db.Column(db.String(254), nullable=False)
    is_staff = db.Column(db.Boolean, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    date_joined = db.Column(db.DateTime, nullable=False)
    # watchlistusers_ = db.relationship("auction_listing_watchlistusers")

    @property
    def passwordhash(self):
        raise AttributeError('password: write-only field')

    @passwordhash.setter
    def passwordhash(self, password):
        self.password = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return flask_bcrypt.check_password_hash(self.password, password)

    @staticmethod
    def encode_auth_token(user_id: int) -> bytes:
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token: str) -> Union[str, int]:
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def __repr__(self):
        return "<User '{}'>".format(self.username)
