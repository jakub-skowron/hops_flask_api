from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

#app & db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret_key"

db = SQLAlchemy(app)

#models
class Hop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    feature = db.Column(db.String(50))
    description = db.Column(db.String(120))

    def __repr__(self) -> str:
        return f"{self.name} - {self.feature} - {self.description}"


@app.route('/hops_list', methods=["GET"])
def get_hops_list():
    hops = Hop.query.all()
    output = []
    for hop in hops:
        hop_data = {
            "id":hop.id, 
            "name":hop.name,
            "feature":hop.feature, 
            "description":hop.description
            }
        output.append(hop_data)
    return {"hops list": output}

@app.route('/hops_list/<int:hop_id>', methods=["GET"])
def get_hops_specification(hop_id: int):
    hop = Hop.query.get_or_404(hop_id)
    return jsonify({
            "id":hop.id, 
            "name":hop.name,
            "feature":hop.feature, 
            "description":hop.description
            })
    
if __name__ == "__main__":
    app.run(debug = True)
