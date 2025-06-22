from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # ← This enables Cross-Origin requests

@app.route("/anomalies")
def anomalies():
    transactions = [{"id": i, "amount": random.randint(10, 10000)} for i in range(1, 11)]
    for tx in transactions:
        tx["flag"] = "Anomaly" if tx["amount"] > 8000 else "Normal"
    return jsonify(transactions)

if __name__ == "__main__":
    app.run(debug=True)
