from flask_api import status

from app import create_app
from app.response.BaseResponse import BaseResponse



if __name__ == 'main':
    app = create_app()
    with app.app_context():
        # TODO: can de something here when server start
        pass
    

# Default 404 response
@app.errorhandler(404)
def page_not_found(e):
    return BaseResponse().error(http_status=status.HTTP_404_NOT_FOUND)


# Before execute request
@app.before_request
def log_request_info():
    # Log every request starting
    app.logger.info('TODO log before route logic execute')