import json
from flask_api import status
from flask import Blueprint, make_response, render_template
from flask import current_app
from flask import request

from flask_wtf.csrf import generate_csrf

from app.helper import ResponseStatusHelper
from app.response.BaseResponse import BaseResponse

from . import *

template_route = Blueprint('template_route', __name__)


# Render Page with csrf token
@template_route.route(base_template_alias + '/index/', methods=['GET'])
def index():
    try:
        resp = make_response(render_template('index.html'))
        csrf_token = generate_csrf()
        resp.set_cookie('csrf_token', csrf_token, secure=True)
        return resp
    except Exception as ex:
        current_app.logger.exception(ex)


# Force all other url to index.html
@template_route.route(base_template_alias + '/<path:filename>', methods=['GET'])
def serve_template(filename):
    return render_template('' + filename + '/index.html')


# TODO: separate to another file
@template_route.route(base_template_alias + '/form', methods=['POST'])
def form():
    resp = BaseResponse()
    try:
        # TODO: need to test, suppose will auto check csrf token
        req_data = json.loads(request.data)
        return resp

    except Exception as ex:
        return resp.error(code=ResponseStatusHelper.UNKNOWN_ERROR, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR, message=ex)

