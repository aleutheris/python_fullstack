from flask import Flask, jsonify
from flask_cors import CORS
import calcpack

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({"message": "Nothing to calculate here"})


@app.route("/add/<int:a>/<int:b>", methods=["GET"])
def add(a, b):
    cp = calcpack.Calcmod(a, b)
    return jsonify({"result": cp.add()})


@app.route("/sub/<int:a>/<int:b>", methods=["GET"])
def sub(a, b):
    cp = calcpack.Calcmod(a, b)
    return jsonify({"result": cp.sub()})


@app.route("/mul/<int:a>/<int:b>", methods=["GET"])
def mul(a, b):
    cp = calcpack.Calcmod(a, b)
    return jsonify({"result": cp.mul()})


@app.route("/div/<int:a>/<int:b>", methods=["GET"])
def div(a, b):
    cp = calcpack.Calcmod(a, b)
    return jsonify({"result": cp.div()})


@app.route("/exp/<int:a>/<int:b>", methods=["GET"])
def exp(a, b):
    cp = calcpack.Expmod(a, b)
    return jsonify({"result": cp.exp()})


if __name__ == "__main__":
    app.run()
