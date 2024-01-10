from http import HTTPStatus

from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session
from sqlalchemy.exc import IntegrityError

from utils.response import make_redirect
from services.message import MessageService
from services.participants import ParticipantService
from utils.response import make_create_response, make_system_error_response, make_bad_request_response, \
    make_success_response

message_blueprint = Blueprint('message', __name__, url_prefix='/message')
message_service = MessageService()


@message_blueprint.route('/create', methods=['POST'])
def create_message():
    try:
        req_data = request.json
        newMessage = message_service.create_message(**req_data)
        return make_create_response("CREATED"), HTTPStatus.CREATED
    except Exception as e:
        return make_system_error_response(str(e)), HTTPStatus.INTERNAL_SERVER_ERROR


@message_blueprint.route('/getAll/<code_room>', methods=['GET'])
def get_all_messages(code_room):
    try:
        messages = message_service.get_message(code_room)
        return make_success_response(messages), HTTPStatus.OK
    except Exception as e:
        return make_system_error_response(str(e)), HTTPStatus.INTERNAL_SERVER_ERROR
