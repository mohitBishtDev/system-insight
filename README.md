# 🧠 System Insight Dashboard

A real-time system monitoring dashboard built with **Python (Flask)** and **React.js**, using **WebSockets** to deliver live system metrics such as CPU usage, memory, disk, and network stats.

---

## 🚀 Tech Stack

| Layer     | Technology               |
|-----------|---------------------------|
| Frontend  | React.js, JavaScript     |
| Backend   | Python, Flask, Flask-SocketIO |
| Realtime  | WebSocket (Socket.IO)    |
| Monitoring| psutil (Python package)  |

---

## ✨ Features

- Live CPU, memory, disk, and network monitoring
- WebSocket-based real-time updates
- Clean and responsive React dashboard
- Python backend with system-level access
- Modular code structure (backend & client separated)

---

## 📁 Project Structure

system_insight/
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ └── venv/
├── client/
│ ├── src/
│ ├── public/
│ └── package.json
└── README.md


---

## ⚙️ How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/YOUR-USERNAME/system-insight.git
cd system-insight

Setup Backend (Python)
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python app.py

Setup Frontend (React)
cd client
npm install
npm start
