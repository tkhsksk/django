from .settings_common import *

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'dev',
        'PASSWORD': 'NMHLJMTS2LWHU28MFBVG',
        'HOST': 'localhost',
    }
}
