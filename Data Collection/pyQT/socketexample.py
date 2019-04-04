from flask_socketio import SocketIO, emit
from flask import Flask

app = Flask(__name__)
socketio = SocketIO(app)


@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    socketio.emit('newnumber', {'number': 1}, namespace='/test')


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


socketio.run(app)
