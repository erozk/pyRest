from flask import request
from flask_restx import Resource

from app.main.util.decorator import token_required
from ..util.dto import AuctionsListingWatchListUsersDto
from ..service.watchlistuser_service import get_a_watchlistitem, save_new_watchlistuser, delete_watchlistuseritem
from typing import Dict, Tuple

api = AuctionsListingWatchListUsersDto.api
_watchlist = AuctionsListingWatchListUsersDto.auctions_listing_watchlistusers


@api.route('/')
class WatchlistUserList(Resource):
    '''Shows a list of all watchlistuseritem, and lets you POST to add new watchlistuseritem'''
    @api.doc('list_watchlistuseritem')
    @api.marshal_list_with(_watchlist)
    def get(self):
        '''List all watchlistuseritem'''
        return 200
        
    @api.expect(_watchlist, validate=True)
    @api.response(201, 'item successfully created.')
    @api.doc('create a new item')
    def post(self) -> Tuple[Dict[str, str], int]:
        '''Create a new watchlistuseritem'''
        data = request.json
        return save_new_watchlistuser(data=data)


@api.route('/<int:id>')
@api.response(404, 'Watchlistuseritem not found')
@api.param('id', 'The watchlistuseritem identifier')
class WatchlistUser(Resource):
    '''Show a single watchlistuser item and lets you delete them'''
    @api.doc('get_item')
    @api.marshal_with(_watchlist)
    def get(self, id):
        '''Fetch a given resource'''
        return get_a_watchlistitem(id)

@api.route('/<int:listingid>/<int:userid>')
@api.response(404, 'Watchlistuseritem not found')
@api.param('listingid', 'The watchlistuseritem listing identifier')
@api.param('userid', 'The watchlistuseritem user identifier')
class WatchlistUsed(Resource):
    @api.doc('delete_watchlistitem_of_user')
    @api.response(204, 'item deleted')
    def delete(self, listingid, userid):
        '''Delete a item given its identifier'''
        delete_watchlistuseritem(listingid,userid)
        return '', 204

    # @api.expect(_watchlist)
    # @api.marshal_with(_watchlist)
    # def put(self, id):
    #     '''Update a task given its identifier'''
    #     return update(id, _watchlist)


