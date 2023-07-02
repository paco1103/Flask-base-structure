from enum import Enum
from flask_caching import Cache
from config import Config

# Prevent circular import
cache = Cache(config=Config().CACHE_CONFIG)

class CacheEnum(Enum):
    CACHE_NAME1 = 'cache_name_1_for_standard_use'


# TODO: write all cache related functions here
def update_cache():
    pass