from .local import *

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
