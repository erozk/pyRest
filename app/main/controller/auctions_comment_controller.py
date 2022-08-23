from flask import request
from flask_restx import Resource

from app.main.util.decorator import token_required
from ..util.dto import AuctionsCommentDto
from ..service.comment_service import delete_comment, get_comment, save_new_comment, get_comments
from typing import Dict, Tuple

api = AuctionsCommentDto.api
_comment = AuctionsCommentDto.auctions_comment


@api.route('/')
class AuctionCommentItem(Resource):
    @api.doc('create_comment')
    @api.expect(_comment)
    @api.marshal_with(_comment, code=201)
    def post(self) -> Tuple[Dict[str, str], int]:
        '''Create a new AuctionCommentItem'''
        data = request.json
        return save_new_comment(data=data)

@api.route('/auction/<listingid>')
@api.param('listingid', 'listing id')
@api.response(404, 'comments not found.')
class AuctionComments(Resource):
    @api.doc('get comments')
    @api.marshal_with(_comment)
    def get(self, listingid):
        """get comments given listing Id"""
        _comment = get_comments(listingid)
        # if not listing:
        #     api.abort(404)
        # else:
        return _comment


@api.route('/<int:id>')
@api.response(404, 'AuctionComments not found')
@api.param('id', 'The AuctionCommentItem identifier')
class AuctionComment(Resource):
    '''Show a single Auctioncomment item and lets you delete them'''
    @api.doc('get_comment')
    @api.marshal_with(_comment)
    def get(self, id):
        '''Fetch a given comment resource'''
        return get_comment(id)


    @api.doc('delete_comment')
    @api.response(204, 'comment deleted')
    def delete(self, id):
        '''Delete a comment given its identifier'''
        delete_comment(id)
        return '', 204

    # @api.expect(_comment)
    # @api.marshal_with(_comment)
    # def put(self, id):
    #     '''Update a comment given its identifier'''
    #     return update(id, _comment)


