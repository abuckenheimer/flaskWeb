# app.py

from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=8000)
