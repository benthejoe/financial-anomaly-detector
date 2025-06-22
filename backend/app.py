
from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/anomalies")
def anomalies():
    # Simulate detection logic
    transactions = [{"id": i, "amount": random.randint(10, 10000)} for i in range(1, 11)]
    for tx in transactions:
        tx["flag"] = "Anomaly" if tx["amount"] > 8000 else "Normal"
    return jsonify(transactions)

if __name__ == "__main__":
    app.run(debug=True)
