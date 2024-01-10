from http import HTTPStatus

from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session
from sqlalchemy.exc import IntegrityError

from utils.response import make_redirect
from services.users import UsersService
from utils.response import make_create_response, make_system_error_response, make_bad_request_response, make_success_response

users_blueprint = Blueprint('users', __name__, url_prefix='/users')
users_service = UsersService()


@users_blueprint.route('/create', methods=['POST'])
def create_user():
    try:
        req_data = request.json

        if req_data.get('password') != req_data.get('re_password'):
            raise ValueError("Passwords don't match!!!")

        req_data.pop('re_password')

        user = users_service.registerUser(req_data)
        return make_create_response(req_data), HTTPStatus.CREATED
    except IntegrityError as e:
        return make_bad_request_response("Username or Email exist!!!"), HTTPStatus.BAD_REQUEST
    except ValueError as e:
        return make_bad_request_response(str(e)), HTTPStatus.BAD_REQUEST
    except Exception as e:
        return make_system_error_response(str(e)), HTTPStatus.INTERNAL_SERVER_ERROR


@users_blueprint.route('/login', methods=['POST'])
def login_user():
    try:
        req_data = request.json
        user = users_service.loginUser(req_data)
        return make_success_response(req_data), HTTPStatus.OK
    except ValueError as e:
        return make_bad_request_response(str(e)), HTTPStatus.BAD_REQUEST
    except Exception as e:
        return make_system_error_response(str(e)), HTTPStatus.INTERNAL_SERVER_ERROR
