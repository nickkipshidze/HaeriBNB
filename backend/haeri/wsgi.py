"""
WSGI config for haeri project.

It exposes the WSGI callable as a module-level variable named ``application``.

Which one of you sickoes use single quotes isntead of double quotes?
What is wrong with you people?
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "haeri.settings")

application = get_wsgi_application()
