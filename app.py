from flask import Flask, jsonify, request

app = Flask(__name__)


hops = [{'hop':'Lubelski', 'feature':'Bitter'},
        {'hop':'Cascade', 'feature':'Aroma'},
        {'hop':'Citra', 'feature':'Aroma'},
        {'hop':'Mosaic', 'feature':'Aroma'},
        {'hop':'Amarillo', 'feature':'Aroma'},
        {'hop':'Columbus', 'feature':'Bitter'}
        ]

@app.route('/hops_list', methods=["GET"])
def get_hops_list():
    result = [x['hop'] for x in hops]
    return jsonify({"Hops list": result})

@app.route('/hops_list/<int:hop_id>', methods=["GET"])
def get_hops_specification(hop_id: int):
    return jsonify({"Hop specification": hops[hop_id]})
    

@app.route('/hops_list/add_new_hop', methods=["POST"])
def add_new_hop():
    hop = {
        'hop': request.json['hop'],
        'feature': request.json['feature'],
        }
    hops.append(hop)
    return jsonify({"Hops list": hops})

@app.route('/hops_list/delete/<int:hop_id>', methods=["DELETE"])
def delete_hop(hop_id: int):
    hops.pop(hop_id)
    return jsonify({"Hops list": hops})

@app.route('/hops_list/update/<int:hop_id>', methods=["PUT"])
def update_hop(hop_id: int):
    hop = {
        'hop': request.json['hop'],
        'feature': request.json['feature'],
        }
    hops[hop_id] = hop
    return jsonify({"Hops list": hops})

if __name__ == "__main__":
    app.run(debug = True)