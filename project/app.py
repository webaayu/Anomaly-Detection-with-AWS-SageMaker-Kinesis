from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
model_path = "./src/model/isolation_forest_model.pkl"
with open(model_path, "rb") as f:
    model = pickle.load(f)

@app.route("/ping", methods=["GET"])
def ping():
    return "OK", 200

@app.route("/invocations", methods=["POST"])
def invoke():
    data = request.json["data"]
    predictions = model.predict(np.array(data))
    response = {"predictions": predictions.tolist()}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
