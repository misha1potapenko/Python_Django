from django.core.management.base import BaseCommand

from secondapp.models import Order
from secondapp.models import Product
from secondapp.models import User

class Command(BaseCommand):
    help = "Create order. Inter id user and id product"

    # def add_arguments(self, parser):
    #     parser.add_argument('id', type=int, help='User ID')
    #     parser.add_argument('id_pr', type=int, help='id product')
    #     parser.add_argument('id_pr2', type=int, help='id product')
    def handle(self, *args, **kwargs):
        # id = kwargs['id']
        # id_pr = kwargs['id_pr']
        # id_pr2 = kwargs['id_pr2']
        user = User.objects.get(id=1)
        product1 = Product.objects.get(id=1)
        product2 = Product.objects.get(id=2)
        self.stdout.write(f'{user}')
        self.stdout.write(f'{product1}')
        self.stdout.write(f'{product2}')
        order = Order(customer=user, all_price=3)
        order.save()
        order.products.add(product1)
        order.products.add(product2)
        order.save()
        self.stdout.write(f'{order}')
