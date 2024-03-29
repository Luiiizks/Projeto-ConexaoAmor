"""
WSGI config for setup project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# para mudar a configuracao usada, se o app for rodado localmente ou na azure
settings_module = 'setup.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'setup.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
