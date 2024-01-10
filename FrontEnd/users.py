from http import HTTPStatus

from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session
import requests

users_front_end = Blueprint('users_fe', __name__)


@users_front_end.route('/', methods=['GET'])
def login_form():
    if session.get('success'):
        username = session.get('success')
        session.clear()
        return render_template("login.html", username=username)
    elif session.get('error'):
        error = str(session.get('error'))
        session.clear()
        return render_template("login.html", error=error)

    session.clear()
    return render_template("login.html")


@users_front_end.route('/register', methods=['GET'])
def register_form():
    if session.get('error'):
        error = str(session.get('error'))
        session.clear()
        return render_template("register.html", error=error)

    return render_template("register.html")


@users_front_end.route('/register', methods=['POST'])
def register_user():
    data = dict(
        username=request.form['username'],
        email=request.form['email'],
        full_name=request.form['full_name'],
        password=request.form['password'],
        re_password=request.form['re_password']
    )

    response = requests.post('http://127.0.0.1:5000/api/v1/users/create', json=data)
    response = response.json()

    if response.get("http_code") == 201:
        session['success'] = response.get('data').get('username')
        return redirect(url_for('users_fe.login_form'))
    elif response.get("http_code") == 400 or response.get("http_code") == 500:
        session['error'] = response.get('err_msg')
        return redirect(url_for('users_fe.register_form'))


@users_front_end.route('/', methods=['POST'])
def login_user():
    data = dict(
        username=request.form['username'],
        password=request.form['pwd']
    )

    response = requests.post('http://127.0.0.1:5000/api/v1/users/login', json=data)
    response = response.json()

    if response.get("http_code") == 200:
        session['username'] = response.get('data').get('username')
        return redirect(url_for('rooms_fe.list_room'))
    elif response.get("http_code") == 400 or response.get("http_code") == 500:
        session['error'] = response.get('err_msg')
        return redirect(url_for('users_fe.login_form'))
