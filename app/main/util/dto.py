from flask_restx import Namespace, fields


class AuctionsUserDto:
    api = Namespace('auctions_user', description='user related operations')
    auctions_user = api.model('auctions_user', {
        'password': fields.String(required=True, description='user password'),
        'is_superuser': fields.Boolean(required=True, description='is superuser'),
        'username': fields.String(required=True, description='user username'),
        'first_name': fields.String(required=True, description='user username'),
        'last_name': fields.String(required=True, description='user username'),
        'email': fields.String(required=True, description='user email address'),
        'is_stuff': fields.Boolean(required=True, description='is stuff')
    })


# class UserDto:
#     api = Namespace('user', description='user related operations')
#     user = api.model('user', {
#         'email': fields.String(required=True, description='user email address'),
#         'username': fields.String(required=True, description='user username'),
#         'password': fields.String(required=True, description='user password'),
#         'public_id': fields.String(description='user Identifier')
#     })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class AuctionsListingDto:
    api = Namespace('auctions_listing', description='auction related operations')
    auctions_listing = api.model('auctions_listing', {
        'id': fields.Integer(description='id'),
        'title': fields.String(required=True, description='title'),
        'description': fields.String(required=True, description='description'),
        'currentBidValue': fields.String(required=True, description='currentBidValue'),
        'imageURL': fields.String(required=True, description='image URL'),
        'isOpen': fields.Boolean(required=True, description='is Open'),
        'user_id': fields.Integer(required=True, description='user id'),
        'winner_id': fields.Integer(required=True, description='winner id'),
        'isFav': fields.Integer(required=False, description='isFav')
    })

class AuctionsListingWatchListUsersDto:
    api = Namespace('auctions_listing_watchlistusers', description='auction watchlistuser related operations')
    auctions_listing_watchlistusers = api.model('auctions_listing_watchlistusers', {
        'id': fields.Integer(description='id'),
        'listing_id': fields.Integer(description='listing_id', required=True),
        'user_id': fields.Integer(description='user_id', required=True),
    })


class AuctionsCommentDto:
    api = Namespace('auctions_comment', description='auctions comment related operations')
    auctions_comment = api.model('auctions_comment', {
        'id': fields.Integer(description='id'),
        'datetime': fields.DateTime(required=True, description='datetime'),
        'content': fields.String(required=True, description='content'),
        'listing_id': fields.Integer(required=True, description='listing_id'),
        'user_id': fields.Integer(required=True, description='user id'),
        'fullName': fields.String(required=False, description='fullName')
    })

class AuctionsBidDto:
    api = Namespace('auctions_bid', description='auctions bid related operations')
    auctions_bid = api.model('auctions_bid', {
        'id': fields.Integer(description='id'),
        'datetime': fields.DateTime(required=True, description='datetime'),
        'value': fields.Integer(required=True, description='value'),
        'listing_id': fields.Integer(required=True, description='listing_id'),
        'user_id': fields.Integer(required=True, description='user id'),
        'fullName': fields.String(required=False, description='fullName')
    })