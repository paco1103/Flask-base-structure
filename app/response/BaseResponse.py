from flask import current_app
from flask_api import status

from app.helper import ResponseStatusHelper

class BaseResponse:

    def __init__(self):
        # TODO: standard response define
        self.response = {
            'success': True,
            'message': '',
            'code': ResponseStatusHelper.ERROR_CODE1,
            'data': {}
        }

    def success(self, data={}):
        # for child class
        self.response['data'] = data
        # log in here
        current_app.logger.info(self.response)
        return self.response, 200

    def fail(self, code):
        self.response['success'] = False
        self.response['code'] = code
        self.response['message'] = ResponseStatusHelper.message(code)
        current_app.logger.warning(self.response)
        return self.response, 200

    def error(self):
        self.response['success'] = False
        current_app.logger.exception(self.response)
        return self.response, status.HTTP_500_INTERNAL_SERVER_ERROR
