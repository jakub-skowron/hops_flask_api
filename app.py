from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

'''
API helps finding hops substitutes
'''
#app & db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mongodb://admin:ifPqBVdO3sGwundRxz593OJY@MongoS3601A.back4app.com:27017/91871e87fb9a4be891a477b0a57d57aa"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret_key"

db = SQLAlchemy(app)

#models
class Hop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    substitutes = db.Column(db.String(120))

    def __repr__(self) -> str:
        return f"{self.name} - {self.substitutes}"


@app.route('/hops_list', methods=["GET"])
def get_hops_list():
    hops = Hop.query.all()
    output = []
    for hop in hops:
        hop_data = {
            "id":hop.id, 
            "name":hop.name,
            "substitutes":hop.substitutes
            }
        output.append(hop_data)
    return {"hops list": output}


@app.route('/hops_list/<int:hop_id>', methods=["GET"])
def get_hops_specification(hop_id: int):
    hop = Hop.query.get_or_404(hop_id)
    return jsonify({
            "id":hop.id, 
            "name":hop.name,
            "substitutes":hop.substitutes
            })


if __name__ == "__main__":
    app.run(debug = True)
