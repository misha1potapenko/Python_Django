from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=150)
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    date_registrations = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'name: {self.name}, email: {self.email}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    count_product = models.DecimalField(max_digits=30, decimal_places=3)
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'name: {self.name}, price: {self.price}, description: {self.description}'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    all_price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ['customer']

    def __str__(self):
        return f'customer: {self.customer}, product: {self.products}, price: {self.all_price}'