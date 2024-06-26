from flask import Flask
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "Chat Server on"

@socketio.on('message')
def handle_message(data):
    message = data.get('message')
    sender = data.get('sender')
    timestamp = data.get('timestamp')
    print(f'Message from {sender} at {timestamp}: {message}')
    send(data, broadcast=True)

@socketio.on('voice_message')
def handle_voice_message(data):
    voice_data = data.get('voice_data')
    sender = data.get('sender')
    timestamp = data.get('timestamp')
    print(f'Voice message from {sender} at {timestamp}')
    emit('voice_message', data, broadcast=True)

@socketio.on('file_message')
def handle_file_message(data):
    file_data = data.get('file_data')
    file_name = data.get('file_name')
    sender = data.get('sender')
    timestamp = data.get('timestamp')
    print(f'File message from {sender} at {timestamp}: {file_name}')
    emit('file_message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
