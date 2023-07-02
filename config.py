import os
import urllib.parse
from dotenv import load_dotenv


# General Config
class Config:
    # Read from os environment variables or .env file
    load_dotenv()

    # Database Config
    db_driver = os.getenv('DATABASE_DRIVER')
    db_server = os.getenv('DATABASE_SERVER')
    db_port = os.getenv('DATABASE_PORT')
    db_name = os.getenv('DATABASE_DATABASE')
    db_user = os.getenv('DATABASE_USER')
    db_password = urllib.parse.quote_plus(os.getenv('DATABASE_PASSWORD'))
    db_ssl_cert_path = os.getenv('SSL_CERT_PATH')

    SQLALCHEMY_DATABASE_URI = '{driver}://{user}:{password}@{server}:{port}/{db}'.format(
        driver=db_driver, user=db_user, password=db_password, server=db_server, port=db_port, db=db_name)

    if db_ssl_cert_path != '':
        SQLALCHEMY_DATABASE_URI += '?ssl_ca={cert_path}'.format(
            cert_path=db_ssl_cert_path)

    # Cache Config
    CACHE_CONFIG = {
        'CACHE_TYPE': 'SimpleCache',  # Candidates: 'SimpleCache', 'FileSystemCache', 'RedisCache
        'CACHE_DEFAULT_TIMEOUT': 0  # 0 = infinity
    }

    SECRET_KEY = os.getenv('CSRF_SECRET_KEY')

    # Logger Config
    LOGGING_CONFIG = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
        },
        'handlers': {
            'default': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'standard',    # name as formatter
                'filename': 'log/example.log',
                'maxBytes': 1024*1024*10,  # 10 mb
                'backupCount': 5,
            },
            'console': {
                'class': 'logging.StreamHandler',   # stream log for console
                'formatter': 'standard',
            },
        },
        'loggers': {
            'root': {  # all logger
                'handlers': ['default', 'console'],
                'level': 'INFO',    # log >= this level, default ERROR
                'propagate': False
            },
        }
    }
