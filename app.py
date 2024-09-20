from web_socket_server import WebSocketServer, socketio, app
from flask import render_template
import json

app = WebSocketServer().create_app()

message_storage  = {}

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(message):
    msg_dict = json.loads(message)
    print(f'Recieved message: {msg_dict}')
    user_sender = msg_dict['user']
    if user_sender in message_storage:
        message_storage[user_sender].append(msg_dict['message'])
    else:
        message_storage[user_sender] = [msg_dict['message']]
    print(message_storage)

@socketio.on('get_all_messages')
def handle_get_user_messages(data, user='JohnDoe'):
    socketio.emit('get_all_messages', message_storage[user])

# @app.route('/')
# def index():
#     return render_template('WebSocketClient.html')

if __name__ == '__main__':
    socketio.run(app)