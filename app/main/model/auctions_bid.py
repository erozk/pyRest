from .. import db

class Auctions_bid(db.Model):
    """ Auctions_bid model for storing bid related details """
    __tablename__ = "auctions_bid"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    datetime = db.Column(db.DateTime, nullable=False)
    value = db.Column(db.Integer,nullable = False)
    listing_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Auctions_bid '{}'>".format(self.id)
