from flask import Flask, jsonify, request

app = Flask(__name__)

enter = [
    {
        'id': 1,
        'tipo': 'Entrada',
        'servico': 'Spa',
        'valor': 2000
    },
    {
        'id': 2,
        'tipo': 'Entrada',
        'servico': 'Piscina',
        'valor': 2000
    },
    {
        'id': 3,
        'tipo': 'Entrada',
        'servico': 'Fotografia',
        'valor': 2000
    }
]


@app.route('/enter', methods=['GET'])
def get_enter():
    return jsonify(enter)


@app.route('/enter/<int:id>', methods=['GET'])
def get_enterid(id):
    for go in enter:
        if go.get('id') == id:
            return jsonify(go)


@app.route('/enter/<int:id>', methods=['PUT'])
def edit_enter(id):
    enter_change = request.get_json()
    for desc,pkenter in enumerate(enter):
        if pkenter.get('id') == id:
            pkenter[desc].update(enter_change)
            return jsonify(pkenter[desc])


@app.route('/enter', methods=['POST'])
def new_enter():
    newenter = request.get_json()
    enter.append(newenter)
    return jsonify(enter)


@app.route('/enter/<int:id>', methods=["DELETE"])
def delete_enter(id):
    for desc, pkenter in enumerate(enter):
        if pkenter.get('id') == id:
            del enter[desc]
    return jsonify(enter)


app.run(port=5000, host='localhost', debug=True)
