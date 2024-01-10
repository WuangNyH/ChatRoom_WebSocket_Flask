from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import join_room, leave_room, send, SocketIO
import random, os
from string import ascii_uppercase
from dotenv import load_dotenv
import requests

from FrontEnd.rooms import rooms_front_end
from routes import routes
from FrontEnd.users import users_front_end

load_dotenv()

app = Flask(__name__)
app.register_blueprint(routes)
app.register_blueprint(users_front_end)
app.register_blueprint(rooms_front_end)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


@socketio.on("message")
def message(data):
    room = session.get("code_room")

    content = {
        "name": session.get("username"),
        "message": data["data"]
    }
    send(content, to=room)
    dataMsg = {
        "code_room": room,
        "content": data["data"],
        "username": session.get("username")
    }
    requests.post("http://127.0.0.1:5000/api/v1/message/create", json=dataMsg)
    print(f"{session.get('username')} said: {data['data']}")


@socketio.on("connect")
def connect(auth):
    room = session.get("code_room")
    name = session.get("username")
    if not room or not name:
        return

    join_room(room)
    send({"name": name, "message": "has entered the room"}, to=room)
    print(f"{name} joined room {room}")


@socketio.on("disconnect")
def disconnect():
    room = session.get("code_room")
    name = session.get("username")
    leave_room(room)
    send({"name": name, "message": "has left the room"}, to=room)
    print(f"{name} has left the room {room}")


if __name__ == "__main__":
    socketio.run(app, debug=True, use_reloader=True)
