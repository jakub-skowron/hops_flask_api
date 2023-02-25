from app import db


class Hop(db.Model):
    __tablename__ = "hops"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    alpha_max_percentage = db.Column(db.Integer, nullable=True)
    alpha_min_percentage = db.Column(db.Integer, nullable=True)
    beta_max_percentage = db.Column(db.Integer, nullable=True)
    beta_min_percentage = db.Column(db.Integer, nullable=True)
    origin = db.Column(db.String(32))
    description = db.Column(db.String(256))
    aroma = db.Column(db.String(256))
    beer_styles = db.Column(db.String(256))
    used_for = db.Column(db.String(32))
    substitutions = db.Column(db.String(256))

    def as_dict(self):
        hop_dict = {
            "id": self.id,
            "name": self.name,
            "alpha_max_percentage": self.alpha_max_percentage,
            "alpha_min_percentage": self.alpha_min_percentage,
            "beta_max_percentage": self.beta_max_percentage,
            "beta_min_percentage": self.beta_min_percentage,
            "origin": self.origin,
            "description": self.description,
            "aroma": self.aroma,
            "beer_styles": self.beer_styles,
            "used_for": self.used_for,
            "substitutions": self.substitutions,
        }
        return hop_dict
