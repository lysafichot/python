from app import app
from flask import render_template, request
import socketio

sio = socketio.Server()


# socketio.run(app, host='localhost', port='5000')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
