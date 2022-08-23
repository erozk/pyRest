from .. import db
class Auctions_listing_losers(db.Model):
    """ Auctions_listing_losers model for storing auction related details """
    __tablename__ = "auctions_listing_losers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    listing_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Auctions_listing_losers '{}'>".format(self.id)
