from .. import db
class Auctions_comment(db.Model):
    """ Auctions_comment model for storing comment related details """
    __tablename__ = "auctions_comment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    datetime = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.String(256),nullable = False)
    listing_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Auctions_comment '{}'>".format(self.id)
