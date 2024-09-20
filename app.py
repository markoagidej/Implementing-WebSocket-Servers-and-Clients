from web_socket_server import WebSocketServer, socketio, app
from flask import render_template

app = WebSocketServer().create_app()

messages = []

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(message):
    print(f'Recieved message: {message}')
    messages.append(message)
    socketio.emit('message', message)

@socketio.on('get_user_messages')
def handle_get_user_messages(data):
    socketio.emit('get_user_messages', messages)

@app.route('/')
def index():
    return render_template('WebSocketClient.html')

if __name__ == '__main__':
    socketio.run(app)