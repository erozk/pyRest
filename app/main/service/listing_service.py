from operator import and_
from datetime import datetime

from sqlalchemy import null
from sqlalchemy import case

from app.main import db
from app.main.model.auctions_listing import Auctions_listing
from app.main.model.auctions_listing_watchlistusers import Auctions_listing_watchlistusers
from app.main.model.auctions_listing_losers import Auctions_listing_losers
from typing import Dict, Tuple


def save_new_listing(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    new_listing = Auctions_listing(
        datetime=datetime.now(),
        title= data['title'],
        description=data['description'],
        currentBidValue=0,
        imageURL=data['imageURL'],
        isOpen= True,
        user_id=data['user_id'],
        winner_id=0
    )
    save_changes(new_listing)
    response_object = {
        'status': 'success',
        'message': 'Successfully created.'
    }
    return response_object, 201


def get_all_listing(userid):
    if (userid != null):
        return db.session.query(Auctions_listing.id, Auctions_listing.title,
                                Auctions_listing.description, Auctions_listing.currentBidValue, Auctions_listing.imageURL, Auctions_listing.isOpen,
                                Auctions_listing.user_id, Auctions_listing.winner_id,
                                case((Auctions_listing_watchlistusers.id > 0, True), else_=False).label("isFav")).join(Auctions_listing_watchlistusers,
                                and_(Auctions_listing_watchlistusers.listing_id == Auctions_listing.id, Auctions_listing_watchlistusers.user_id == userid), \
                                isouter=True).filter(Auctions_listing.isOpen == True).all()
    else:
        return db.session.query(Auctions_listing).all()


def get_a_listing(id):
    return Auctions_listing.query.filter_by(id=id).first()


def get_watchlist_users(userid):
    # return Auctions_listing.query.join(Auctions_listing_watchlistusers, Auctions_listing.id == Auctions_listing_watchlistusers.listing_id).filter(Auctions_listing_watchlistusers.user_id == userid).all()
    return db.session.query(Auctions_listing.id, Auctions_listing.title,
                            Auctions_listing.description, Auctions_listing.currentBidValue, Auctions_listing.imageURL, Auctions_listing.isOpen,
                            Auctions_listing.user_id, Auctions_listing.winner_id,
                            case((Auctions_listing_watchlistusers.id > 0, True), else_=False).label("isFav")).join(Auctions_listing_watchlistusers, \
                            and_(Auctions_listing_watchlistusers.listing_id == Auctions_listing.id, Auctions_listing_watchlistusers.user_id == userid)).all()


def get_wonauctions_list(userid):
    # return Auctions_listing.query.filter(Auctions_listing.winner_id == userid).all()
    return db.session.query(Auctions_listing.id, Auctions_listing.title,
                            Auctions_listing.description, Auctions_listing.currentBidValue, Auctions_listing.imageURL, Auctions_listing.isOpen,
                            Auctions_listing.user_id, Auctions_listing.winner_id,
                            case((Auctions_listing_watchlistusers.id > 0, True), else_=False).label("isFav")).join(Auctions_listing_watchlistusers, \
                            and_(Auctions_listing_watchlistusers.listing_id == Auctions_listing.id, Auctions_listing_watchlistusers.user_id == userid), \
                            isouter=True).filter(Auctions_listing.winner_id == userid).all()


def get_lost_auctions_list(userid):
    # return Auctions_listing.query.join(Auctions_listing_losers, Auctions_listing.id == Auctions_listing_losers.listing_id).filter(Auctions_listing_losers.user_id == userid).all()
    return db.session.query(Auctions_listing.id, Auctions_listing.title,
                            Auctions_listing.description, Auctions_listing.currentBidValue, Auctions_listing.imageURL, Auctions_listing.isOpen,
                            Auctions_listing.user_id, Auctions_listing.winner_id,
                            case((Auctions_listing_watchlistusers.id > 0, True), else_=False).label("isFav")) \
                            .join(Auctions_listing_watchlistusers, and_(Auctions_listing_watchlistusers.listing_id == Auctions_listing.id,\
                            Auctions_listing_watchlistusers.user_id == userid), isouter=True).join(Auctions_listing_losers, \
                             Auctions_listing.id == Auctions_listing_losers.listing_id).filter(Auctions_listing_losers.user_id == userid).all()


def save_changes(data: Auctions_listing) -> None:
    db.session.add(data)
    db.session.commit()

def update_value(data,_id) ->  Tuple[Dict[str, str], int]:
    auction = Auctions_listing.query.filter_by(id=_id).first()
    auction.currentBidValue = data['currentBidValue']
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Successfully updated.'
    }
    return response_object, 201

def update_value_close(data,_id) ->  Tuple[Dict[str, str], int]:
    auction = Auctions_listing.query.filter_by(id=_id).first()
    auction.isOpen = data['isOpen']
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Successfully updated.'
    }
    return response_object, 201


