from .common import *

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = 'w-r7j8s_95as8q*h@%c-jky8@0!b3@b2&e6tvqz*2)dxr&&a(^'

# Location of root django.contrib.admin URL, use {% url 'admin:index' %}
ADMIN_URL = r'^admin/'

ALLOWED_HOSTS = [
    'localhost',
]

JWT_AUTH['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=7)
JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA'] = datetime.timedelta(days=7)
