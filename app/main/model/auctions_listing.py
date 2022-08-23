from .. import db
class Auctions_listing(db.Model):
    """ auction listing model for storing auction related details """
    __tablename__ = "auctions_listing"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    datetime = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(256), nullable =False)
    currentBidValue = db.Column(db.Integer, nullable =False)
    imageURL= db.Column(db.String(256), nullable =False)
    isOpen = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    winner_id = db.Column(db.Integer, nullable=False)
    # watchlistusers = db.relationship("auction_listing_watchlistusers")

    def __repr__(self):
        return "<Listing '{}'>".format(self.title)
