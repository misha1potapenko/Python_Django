from django.core.management.base import BaseCommand

from secondapp.models import Product

class Command(BaseCommand):
    help = "Create product."
    def handle(self, *args, **kwargs):
        for i in range(1, 100):
            product = Product(name=f'butter{i}', price=1.99, description=f"for lunch{i}",
                                             count_product=126)
            product.save()
            self.stdout.write(f'{product}')