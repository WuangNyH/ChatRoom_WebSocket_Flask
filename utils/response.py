from http import HTTPStatus

from flask import make_response


def make_redirect(code, url):
    response = make_response(url)
    response.status_code = code
    return response


def make_success_response(data):
    return {
        "http_code": HTTPStatus.OK,
        "err_msg": {},
        "data": data,
    }


def make_create_response(data):
    return {
        "http_code": HTTPStatus.CREATED,
        "err_msg": {},
        "data": data,
    }


def make_system_error_response(content: str):
    return {
        "http_code": HTTPStatus.INTERNAL_SERVER_ERROR,
        "err_msg": content,
        "data": [],
    }


def make_bad_request_response(message: str = None):
    return {
        "http_code": HTTPStatus.BAD_REQUEST,
        "err_msg": message,
        "data": [],
    }
