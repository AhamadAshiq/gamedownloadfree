from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Creates an admin user'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = os.getenv('DJANGO_ADMIN_USERNAME', 'admin')
        email = os.getenv('DJANGO_ADMIN_EMAIL', 'admin@example.com')
        password = os.getenv('DJANGO_ADMIN_PASSWORD', 'admin123')

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created successfully."))
        else:
            self.stdout.write(self.style.WARNING(f"Superuser '{username}' already exists."))
