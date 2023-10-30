from django.core.management.base import BaseCommand
from blog.models import User


class Command(BaseCommand):
    help = "Create user."
    list_user = ['Pavel', 'Mike', 'Ilia', 'Vova', 'Kirill','Lena', 'Petr', 'Zina', 'Victor']
    def handle(self, *args, **kwargs):
        list_user = ['Pavel', 'Mike', 'Ilia', 'Vova', 'Kirill', 'Lena', 'Petr', 'Zina', 'Victor']
        for i in list_user:
            user = User(name=f'{i}', email=f'{i}@example.com', phone_number=545555, address="street", password=f'secret{i}', age=25)
            user.save()
            self.stdout.write(f'{user}')