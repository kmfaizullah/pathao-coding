#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from decouple import config
from apps.core.constants import PRODUCTION_SERVER, DEVELOPMENT_SERVER, STAGE_SERVER

def main():
    """Run administrative tasks."""
    server_name = config('SERVER_NAME')
    if server_name == DEVELOPMENT_SERVER:
        settings_name = 'config.settings.development'
    elif server_name == STAGE_SERVER:
        settings_name = 'config.settings.stage'
    elif server_name == PRODUCTION_SERVER:
        settings_name = 'config.settings.production'

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_name)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
