from datetime import datetime
from operator import concat
from app.main import db
from app.main.model.auctions_bid import Auctions_bid
from app.main.model.auctions_user import Auctions_user
from typing import Dict, Tuple


def save_new_bid(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    new_item = Auctions_bid(
        datetime=datetime.now(),
        value=data['value'],
        listing_id=data['listing_id'],
        user_id=data['user_id'],
    )
    save_changes(new_item)
    response_object = {
        'status': 'success',
        'message': 'Successfully created.'
    }
    return response_object, 201


def get_bids(listing_id):
    return db.session.query(Auctions_bid.datetime, Auctions_bid.value,(Auctions_user.first_name +" " +  Auctions_user.last_name).label('fullName')).join(Auctions_user, \
             Auctions_user.id == Auctions_bid.user_id).filter(Auctions_bid.listing_id == listing_id).all()
 # return Auctions_bid.query.filter(Auctions_bid.listing_id == listing_id).all()


def get_bid(id):
    return Auctions_bid.query.filter_by(Auctions_bid.id == id).first()


def delete_bid(id):
    item = db.session.get(Auctions_bid, id)
    db.session.delete(item)
    db.session.commit()


def save_changes(data: Auctions_bid) -> None:
    db.session.add(data)
    db.session.commit()
