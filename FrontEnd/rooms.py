from http import HTTPStatus

from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session
import requests

rooms_front_end = Blueprint('rooms_fe', __name__)


@rooms_front_end.route('/chat-room/<string:code_room>', methods=["GET"])
def chat_room(code_room):
    session["code_room"] = code_room

    messages = requests.get(f"http://127.0.0.1:5000/api/v1/message/getAll/{code_room}")
    messages = messages.json().get("data")
    print(messages)

    return render_template("chat-room.html", messages=messages, username=session["username"])


@rooms_front_end.route('/list-room', methods=['GET'])
def list_room():
    response = requests.get(f'http://127.0.0.1:5000/api/v1/rooms/getAll/{session.get("username")}')
    response = response.json()

    if session.get('error'):
        error = str(session.get('error'))
        session.pop("error", None)
        return render_template("list-room.html", error=error, rooms=response.get("data"))

    return render_template('list-room.html', rooms=response.get("data"))


@rooms_front_end.route('/create-room', methods=['POST'])
def create_room():
    data = dict(
        username=session['username'],
        room_name=request.form['room_name']
    )

    response = requests.post('http://127.0.0.1:5000/api/v1/rooms/create', json=data)
    response = response.json()

    if response.get("http_code") == 201:
        session["room"] = response.get("data").get("code_room")
        return redirect(url_for('rooms_fe.chat_room', code_room=response.get("data").get("code_room")))
    elif response.get("http_code") == 500:
        session['error'] = response.get('err_msg')
        return redirect(url_for('rooms_fe.list_room'))


@rooms_front_end.route('/join-room', methods=['POST'])
def join_room():
    room_code = request.form['room_code']
    session["room"] = room_code
    data = {
        "name": session['username'],
        "code_room": room_code
    }
    requests.post("http://127.0.0.1:5000/api/v1/participants/create", json=data)
    return redirect(url_for('rooms_fe.chat_room', code_room=room_code))
