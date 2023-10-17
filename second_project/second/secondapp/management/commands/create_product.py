from django.core.management.base import BaseCommand

from secondapp.models import Product

class Command(BaseCommand):
    help = "Create product."
    def handle(self, *args, **kwargs):
        product = Product(name='butter', price=1.99, description="for lunch",
                    count_product=126)
        product.save()
        self.stdout.write(f'{product}')