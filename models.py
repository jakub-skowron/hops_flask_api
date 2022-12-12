from app import db

class Hop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    alpha = db.Column(db.String(32))
    beta = db.Column(db.String(32))
    origin = db.Column(db.String(32))
    description = db.Column(db.String(256))
    aroma = db.Column(db.String(256))
    typical_beer_styles = db.Column(db.String(256))
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
            "typical_beer_styles": self.typical_beer_styles,
            "used_for": self.used_for,
            "substitutions": self.substitutions
        }
        return hop_dict
