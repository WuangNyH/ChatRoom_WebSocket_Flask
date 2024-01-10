from http import HTTPStatus

from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session

from utils.response import make_redirect
from services.participants import ParticipantService
from utils.response import make_create_response, make_system_error_response, make_bad_request_response, \
    make_success_response

participants_blueprint = Blueprint('participants', __name__, url_prefix='/participants')
participants_service = ParticipantService()


@participants_blueprint.route('/create', methods=['POST'])
def create():
    try:
        req_data = request.json
        newParticipant = participants_service.create_participant(**req_data)
        return make_create_response("CREATED"), HTTPStatus.CREATED
    except Exception as e:
        return make_system_error_response(str(e)), HTTPStatus.INTERNAL_SERVER_ERROR
