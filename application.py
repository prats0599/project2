import os

from flask import Flask, render_template, session, redirect
from flask_socketio import SocketIO, emit
from helpers import login_required

app = Flask(__name__)
app.config["SECRET_KEY"] = 'shhhh'
socketio = SocketIO(app)

#keeps track of all channels and all users logged in
channels = []
usersloggedin = []

#instantiate a dictionary for all messages in the channel
channelmsgs = dict()
limit = 100

@app.route("/")
#@login_required
def index():

    return render_template("main.html", channels=channels)

@app.route("/signin")
def signin():
    return render_template("mainp.html", channels=channels)





if __name__ == "__main__":
    socketio.run(app)
