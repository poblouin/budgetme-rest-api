from .common import *

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'budgetme',
        'USER': env.str('POSTGRES_USER_DEBUG'),
        'PASSWORD': env.str('POSTGRES_PASSWORD_DEBUG'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = 'w-r7j8s_95as8q*h@%c-jky8@0!b3@b2&e6tvqz*2)dxr&&a(^'

# Location of root django.contrib.admin URL, use {% url 'admin:index' %}
ADMIN_URL = r'^admin/'

# SITE CONFIGURATION
# ------------------------------------------------------------------------------
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    'localhost:4200',
    'localhost:8000',
    'localhost'
]
# END SITE CONFIGURATION

JWT_AUTH['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=7)
JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA'] = datetime.timedelta(days=7)
