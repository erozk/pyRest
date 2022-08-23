from app.main import db
from app.main.model.auctions_listing_watchlistusers import Auctions_listing_watchlistusers
from typing import Dict, Tuple


def save_new_watchlistuser(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        new_item = Auctions_listing_watchlistusers(
            listing_id= data['listing_id'],
            user_id=data['user_id'],
        )
        save_changes(new_item)
        response_object = {
            'status': 'success',
            'message': 'Successfully created.'
        }
        return response_object, 201



def get_a_watchlistitem(_id):
    return Auctions_listing_watchlistusers.query.filter_by(id=_id).first()

def delete_watchlistuseritem(listingid,userid):
    item = Auctions_listing_watchlistusers.query.filter(Auctions_listing_watchlistusers.listing_id == listingid, Auctions_listing_watchlistusers.user_id == userid).first()
    # db.session.get(Auctions_listing_watchlistusers, id)
    db.session.delete(item)
    db.session.commit()

def save_changes(data: Auctions_listing_watchlistusers) -> None:
    db.session.add(data)
    db.session.commit()

