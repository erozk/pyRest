from flask import request
from flask_restx import Resource


from app.main.util.decorator import token_required
from ..util.dto import AuctionsBidDto
from typing import Dict, Tuple
from app.main.service.bid_service import delete_bid, get_bid, get_bids, save_new_bid

api = AuctionsBidDto.api
_bid = AuctionsBidDto.auctions_bid


@api.route('/')
class AuctionBidItem(Resource):
    @api.doc('create_bid')
    @api.expect(_bid)
    @api.marshal_with(_bid, code=201)
    def post(self) -> Tuple[Dict[str, str], int]:
        '''Create a new AuctionBidItem'''
        data = request.json
        return save_new_bid(data=data)

@api.route('/auction/<listingid>')
@api.param('listingid', 'listing id')
@api.response(404, 'bids not found.')
class AuctionBids(Resource):
    @api.doc('get bids')
    @api.marshal_with(_bid)
    def get(self, listingid):
        """get bids given listing Id"""
        _bid = get_bids(listingid)
        # if not listing:
        #     api.abort(404)
        # else:
        return _bid


@api.route('/<int:id>')
@api.response(404, 'AuctionBids not found')
@api.param('id', 'The AuctionBid item identifier')
class AuctionBid(Resource):
    '''Show a single AuctionBid item and lets you delete them'''
    @api.doc('get_bid')
    @api.marshal_with(_bid)
    def get(self, id):
        '''Fetch a given bid resource'''
        return get_bid(id)


    @api.doc('delete_bid')
    @api.response(204, 'bid deleted')
    def delete(self, id):
        '''Delete a bid given its identifier'''
        delete_bid(id)
        return '', 204

    # @api.expect(_bid)
    # @api.marshal_with(_bid)
    # def put(self, id):
    #     '''Update a bid given its identifier'''
    #     return update(id, _bid)


