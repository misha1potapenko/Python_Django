from django.core.management.base import BaseCommand
from secondapp.models import Order, User


class Command(BaseCommand):
    help = "Get all orders user id."
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            all_orders = Order.objects.filter(customer=user.id)
            self.stdout.write(f'{all_orders}')
