from flask import Flask, jsonify, request
import dbRoom as r;
import dbPass as p;

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/hospedagem')
def get_rom():
    return jsonify(r.room_db)


@app.post('/hospedagem')
def post_rom():
    data = request.get_json()
    r.room_db.append(data)
    return jsonify(data), 200


@app.route('/passagens')
def get_pass():
    return jsonify(p.pass_db)


@app.post('/passagens')
def post_pass():
    data = request.get_json()
    p.pass_db.append(data)
    return jsonify(data), 200


app.run()