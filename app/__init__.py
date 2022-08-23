from flask_restx import Api

from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.auction_controller import api as listing_ns
from .main.controller.watchlistitem_controller import api as watchlistuser_ns
from .main.controller.auctions_bid_controller import api as bid_ns
from .main.controller.auctions_comment_controller import api as comment_ns

blueprint = Blueprint('api', __name__)
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    blueprint,
    title='Auction API',
    version='1.0',
    description='Auction API',
    authorizations=authorizations,
    security='apikey'
)
 

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(listing_ns)
api.add_namespace(watchlistuser_ns)
api.add_namespace(bid_ns)
api.add_namespace(comment_ns)



