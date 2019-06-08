from .base import *
from  .key import SECRET_KEY


DEBUG = False
ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
