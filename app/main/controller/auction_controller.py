from distutils.command.config import config
import os
from flask import request, jsonify
from flask_restx import Resource,reqparse
from sqlalchemy import null
from werkzeug.utils import secure_filename
import werkzeug
from app.main.config import Config

from app.main.util.decorator import token_required
from ..util.dto import AuctionsListingDto
from ..service.listing_service import get_watchlist_users, get_lost_auctions_list, get_wonauctions_list, save_new_listing, get_all_listing, get_a_listing, update_value, update_value_close
from typing import Dict, Tuple

api = AuctionsListingDto.api
_listing = AuctionsListingDto.auctions_listing



ALLOWED_EXTENSIONS = set(['jpeg', 'jpg', 'png', 'gif'])

file_upload = reqparse.RequestParser()
file_upload.add_argument('input_file',
                         type=werkzeug.datastructures.FileStorage,
                         location='files',
                         required=True,
                         help='Input file (images) containing auction image')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@api.route('/')
class AuctionList(Resource):
    @api.doc('list_of_auctions')
    # @token_required
    @api.marshal_list_with(_listing)
    def get(self):
        """List all registered auction listings"""
        return get_all_listing(null)

    @api.expect(_listing, validate=True)
    @api.response(201, 'listing successfully created.')
    @api.doc('create a new listing')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new listing """
        data = request.json
        return save_new_listing(data=data)

@api.route('/upload/')
class my_file_upload(Resource):
    @api.expect(file_upload)
    @api.doc('jpg, jpeg, png, gif allowed only')
    def post(self):
        """jpg, jpeg, png, gif allowed only"""
        if not os.path.exists(Config.UPLOAD_FOLDER):
            os.makedirs(Config.UPLOAD_FOLDER)
        args = file_upload.parse_args()
        args['input_file'].save(os.path.join(Config.UPLOAD_FOLDER,secure_filename(args['input_file'].filename)))
        resp = jsonify({
                'status': 'Success',
                'message' : 'Successfully uploaded',
                'link': args['input_file'].filename})
        resp.status_code = 201
        return resp



@api.route('/listings/<userId>')
@api.param('userId', 'Optional user id')
@api.response(404, 'Listings not found.')
class AuctionsByUser(Resource):
    @api.doc('get all listings of user')
    @api.marshal_with(_listing)
    def get(self, userId):
        """get listings given user Id"""
        listing = get_all_listing(userId)
        # if not listing:
        #     api.abort(404)
        # else:
        return listing


@api.route('/<id>')
@api.param('id', 'The listing id')
@api.response(404, 'Listing not found.')
class Auction(Resource):
    @api.doc('get a listing')
    @api.marshal_with(_listing)
    def get(self, id):
        """get a listing given its identifier"""
        listing = get_a_listing(id)
        # if not listing:
        #     api.abort(404)
        # else:
        return listing

    @api.expect(_listing, validate=True)
    @api.response(201, 'listing successfully updated.')
    @api.doc('update listing current bid value')
    def patch(self,id) -> Tuple[Dict[str, str], int]:
        """Updates listing curent bid value """
        data = request.json
        return update_value(data,id)

@api.route('/close/<id>')
@api.param('id', 'The listing id')
@api.response(404, 'Listing not found.')
class AuctionClose(Resource):
    @api.expect(_listing, validate=True)
    @api.response(201, 'listing successfully updated.')
    @api.doc('update listing open / close value')
    def patch(self,id) -> Tuple[Dict[str, str], int]:
        """Updates listing open / close """
        data = request.json
        return update_value_close(data,id)


@api.route('/watchlist/<userid>')
@api.param('userid', 'The user id')
@api.response(404, 'Watchlist not found.')
class AuctionWatchList(Resource):
    @api.doc('get watchlist')
    @api.marshal_with(_listing)
    def get(self, userid):
        """get watchlist given userid"""
        listing = get_watchlist_users(userid)
        # if not listing:
        #     api.abort(404)
        # else:
        return listing


@api.route('/lost/<userid>')
@api.param('userid', 'The user id')
@api.response(404, 'Lost auctions not found.')
class AuctionLostList(Resource):
    @api.doc('get lost auctions')
    @api.marshal_with(_listing)
    def get(self, userid):
        """get loserlist given userid"""
        listing = get_lost_auctions_list(userid)
        # if not listing:
        #     api.abort(404)
        # else:
        return listing


@api.route('/won/<userid>')
@api.param('userid', 'The user id')
@api.response(404, 'Won auctions not found.')
class AuctlionWonList(Resource):
    @api.doc('get won auctions')
    @api.marshal_with(_listing)
    def get(self, userid):
        """get won list given userid"""
        listing = get_wonauctions_list(userid)
        # if not listing:
        #     api.abort(404)
        # else:
        return listing
