from flask import Flask, jsonify
from flask_socketio import SocketIO
from diagnostics import get_system_metrics
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/api/metrics', methods=['GET'])
def metrics():
    data = get_system_metrics()
    return jsonify(data)

def stream_metrics():
    while True:
        data = get_system_metrics()
        socketio.emit('metrics', data)
        time.sleep(2)

@socketio.on('connect')
def handle_connect():
    print("Client connected")

if __name__ == '__main__':
    threading.Thread(target=stream_metrics).start()
    socketio.run(app, host='0.0.0.0', port=5000)
