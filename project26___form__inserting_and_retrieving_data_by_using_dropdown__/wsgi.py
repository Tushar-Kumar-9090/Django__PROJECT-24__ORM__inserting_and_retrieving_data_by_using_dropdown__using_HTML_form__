"""
WSGI config for project26___form__inserting_and_retrieving_data_by_using_dropdown__ project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project26___form__inserting_and_retrieving_data_by_using_dropdown__.settings')

application = get_wsgi_application()
