from datetime import datetime
from app.main import db
from app.main.model.auctions_comment import Auctions_comment
from app.main.model.auctions_user import Auctions_user
from typing import Dict, Tuple


def save_new_comment(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    new_item = Auctions_comment(
        datetime=datetime.now(),
        content=data['content'],
        listing_id=data['listing_id'],
        user_id=data['user_id'],
    )
    save_changes(new_item)
    response_object = {
        'status': 'success',
        'message': 'Successfully created.'
    }
    return response_object, 201


def get_comments(listing_id):
    return db.session.query(Auctions_comment.datetime, Auctions_comment.content, (Auctions_user.first_name + " " + Auctions_user.last_name).label('fullName')) \
    .join(Auctions_user,Auctions_user.id == Auctions_comment.user_id).filter(Auctions_comment.listing_id == listing_id).all()
# return Auctions_comment.query.filter(Auctions_comment.listing_id == listing_id).all()


def get_comment(id):
    return Auctions_comment.query.filter_by(Auctions_comment.id == id).first()


def delete_comment(id):
    item = db.session.get(Auctions_comment, id)
    db.session.delete(item)
    db.session.commit()


def save_changes(data: Auctions_comment) -> None:
    db.session.add(data)
    db.session.commit()
