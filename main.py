from random import random
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    input_image = request.json[0]
    random_number = random()
    return jsonify({"prob": random_number})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)