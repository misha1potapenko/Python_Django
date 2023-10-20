from django.core.management.base import BaseCommand

from secondapp.models import User

class Command(BaseCommand):
    help = "Create user."
    def handle(self, *args, **kwargs):
        for i in range(1, 100):
            user = User(name=f'Petr{i}', email=f'petr{i}@example.com', address="17 Street Popov",
                        phone_number=8521145226, password='secret3', age=27)
            user.save()
            self.stdout.write(f'{user}')
