"""
WSGI config for gamedownloadfree project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gamedownloadfree.settings')

application = get_wsgi_application()

import os
from django.contrib.auth import get_user_model

def create_superuser():
    User = get_user_model()
    username = os.getenv("DJANGO_ADMIN_USERNAME", "admin")
    email = os.getenv("DJANGO_ADMIN_EMAIL", "admin@example.com")
    password = os.getenv("DJANGO_ADMIN_PASSWORD", "admin123")

    if not User.objects.filter(username=username).exists():
        print("Creating superuser...")
        User.objects.create_superuser(username=username, email=email, password=password)
    else:
        print("Superuser already exists.")

create_superuser()
