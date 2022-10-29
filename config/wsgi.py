"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""
import os
from decouple import config
from apps.core.constants import PRODUCTION_SERVER, DEVELOPMENT_SERVER, STAGE_SERVER
from django.core.wsgi import get_wsgi_application

server_name = config('SERVER_NAME')

settings_name = 'config.settings.development'

if server_name == DEVELOPMENT_SERVER:
    settings_name = 'config.settings.development'
elif server_name == STAGE_SERVER:
    settings_name = 'config.settings.stage'
elif server_name == PRODUCTION_SERVER:
    settings_name = 'config.settings.production'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_name)

application = get_wsgi_application()
