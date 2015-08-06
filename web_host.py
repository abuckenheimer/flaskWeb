# app.py
from markdown2 import markdown_path
from flask.ext.socketio import SocketIO, emit
import os

from flask import *

app = Flask(__name__)
socketio = SocketIO(app)

# class Post(object):
#     def __init__(self, file):
#         self.file = file

posts = os.listdir('./templates/posts')
posts.remove('md')

print posts

@app.route('/')
def index():
    return render_template('landing.html', posts=posts)


@app.route('/contact')
def contact():
    return render_template('contact.html', posts=posts)

@app.route('/code')
def code():
    return render_template('code.html', posts=posts)

@app.route('/blog/<string:post_name>')
def blog(post_name):
    if post_name in posts:
        return render_template('posts/{}.html'.format(post_name), posts=posts)

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/websockets')
def websockets():
    return render_template('index.html', posts=posts)

@socketio.on('my event', namespace='/test')
def test_message(message):
    print "my event", message
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
    print "my broadcast event", message
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
    print "my connect"
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print "my disconnect"
    print('Client disconnected')


if __name__ == '__main__':
    app.debug = True
    socketio.run(app)
