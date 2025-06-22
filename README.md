
# 💰 Financial Data Anomaly Detection Prototype

This is a prototype system that detects irregular patterns in transaction datasets and presents the results via a React-style UI. It's designed to demonstrate how backend anomaly detection can support financial compliance workflows.

---

## 🧩 Project Structure

```
financial-anomaly-detector/
├── backend/
│   └── app.py          # Python Flask API for anomaly detection
└── frontend/
    └── index.html      # Lightweight UI (React-like) to view anomalies
```

---

## 🚀 Features

- **Anomaly Detection Logic**: Flags transactions over a set threshold as anomalies.
- **REST API**: Flask backend serves JSON data to frontend.
- **Frontend Dashboard**: Presents anomalies in a clean, readable table.
- **Simulated Financial Dataset**: Uses randomized transaction data.

---

## 🛠️ How to Run

### 1. Start the Flask Backend

```bash
cd backend
pip install flask
python app.py
```

This runs the API at `http://localhost:5000/anomalies`.

### 2. Open the Frontend

Open `frontend/index.html` in your web browser. It will fetch and display transaction data.

---

## 📈 Example Output

Sample anomaly detection result:

| ID | Amount | Flag     |
|----|--------|----------|
| 1  | 9500   | Anomaly  |
| 2  | 4200   | Normal   |

---

## ✅ Impact

1. Created a Python-based system to detect irregular patterns in transaction datasets.  
2. Used a React-style frontend to display insights, improving financial compliance tooling.

---

## 📄 License

MIT License
