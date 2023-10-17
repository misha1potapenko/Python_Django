from django.core.management.base import BaseCommand

from secondapp.models import User

class Command(BaseCommand):
    help = "Create user."
    def handle(self, *args, **kwargs):
        user = User(name='Petr', email='petr@example.com', address="17 Street Popov",
                    phone_number=8521145226, password='secret3', age=27)
        user.save()
        self.stdout.write(f'{user}')
