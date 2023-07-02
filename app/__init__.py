import logging
import logging.config

from flask import Flask

from config import Config
from .route.ApiRoute import api_route
from .route.TemplateRoute import template_route
from .model import db
from .helper.CacheHelper import cache


def create_app():
    app = Flask(__name__)

    # Logger
    logging.config.dictConfig(Config().LOGGING_CONFIG)

    # Config
    app.config.from_object("config.Config")

    # Cache
    cache.init_app(app)
    
    # Database 
    db.init_app(app)
    with app.app_context():
        # init table
        db.create_all()

    # Route
    # TODO: Register for new route
    app.register_blueprint(api_route)
    app.register_blueprint(template_route)

    return app
