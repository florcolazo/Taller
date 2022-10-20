from api_config import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey("product.id"))
    user = db.relationship("Usuario")
