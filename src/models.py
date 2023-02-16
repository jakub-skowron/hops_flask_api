import json

from app import db


class Hop(db.Model):
    __tablename__ = "hops"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    alpha = db.Column(db.String)
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
            "substitutions": self.substitutions
        }
        return hop_dict

    # def update(self, **kwargs):
        
#hop = Hop(id=1, name="Citra", alpha={"max": "10", "min": "12"}, beta={"max": "10", "min": "12"}, origin="US", description="Lorem...", aroma="citrus", beer_styles={"style": "ale"},used_for="bitterness", substitutions = "None")