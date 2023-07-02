from flask import Blueprint, request
from app.model.Example import Example
from app.response.example.ExampleResponse import ExampleResponse

from . import *

api_route = Blueprint('api_route', __name__)


@api_route.route(base_api_alias + '/example', methods=['GET'])
def example():
    resp = ExampleResponse()
    try:
        try:
            data = request.json
        except Exception as ex:
            # request data format is not application/json
            return resp.error()

        # TODO: api logic
        Example('TODO').save()

        return resp.success()
    except Exception as ex:
        return resp.error()

