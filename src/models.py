from app import db, app
from werkzeug.security import generate_password_hash, check_password_hash


class Hop(db.Model):
    __tablename__ = "hops"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    alpha = db.Column(db.JSON)
    beta = db.Column(db.JSON)
    origin = db.Column(db.String(32))
    description = db.Column(db.String(256))
    aroma = db.Column(db.String(256))
    beer_styles = db.Column(db.JSON)
    used_for = db.Column(db.String(32))
    substitutions = db.Column(db.String(256))

    def as_dict(self):
        hop_dict = {
            "id": self.id,
            "name": self.name,
            "alpha": self.alpha,
            "beta": self.beta,
            "origin": self.origin,
            "description": self.description,
            "aroma": self.aroma,
            "beer_styles": self.beer_styles,
            "used_for": self.used_for,
            "substitutions": self.substitutions,
        }
        return hop_dict

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))

    def hash_password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)