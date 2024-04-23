from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import join_room, leave_room, send, emit, SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template("home.html")

if __name__ == '__main__':
	socketio.run(app, host='0.0.0.0', port=81, debug=True)
