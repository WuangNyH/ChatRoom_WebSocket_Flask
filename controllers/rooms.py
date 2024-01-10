from http import HTTPStatus

from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session
from sqlalchemy.exc import IntegrityError

from utils.response import make_redirect
from services.rooms import RoomService
from services.participants import ParticipantService
from utils.response import make_create_response, make_system_error_response, make_bad_request_response, \
    make_success_response

rooms_blueprint = Blueprint('rooms', __name__, url_prefix='/rooms')
rooms_service = RoomService()
participants_service = ParticipantService()


@rooms_blueprint.route('/create', methods=['POST'])
def create_room():
    try:
        req_data = request.json
        create_data = dict(
            room_name=req_data.get('room_name'),
            created_by=req_data.get('username')
        )
        room = rooms_service.create_room(create_data)
        participants_service.create_participant(code_room=room.code_room, name=req_data.get('username'))
        return make_create_response(dict(code_room=room.code_room, username=req_data['username'], room_name=req_data['room_name'])), HTTPStatus.CREATED
    except Exception as e:
        return make_system_error_response(str(e)), HTTPStatus.INTERNAL_SERVER_ERROR


@rooms_blueprint.route('/getAll/<username>', methods=['GET'])
def get_all_rooms(username):
    try:
        rooms = rooms_service.list_rooms(username)
        return make_success_response(rooms), HTTPStatus.OK
    except Exception as e:
        return make_system_error_response(str(e)), HTTPStatus.INTERNAL_SERVER_ERROR
