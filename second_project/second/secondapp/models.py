from django.db import models

# Создайте три модели Django: клиент, товар и заказ.
#
# Клиент может иметь несколько заказов. Заказ может содержать несколько товаров.
# Товар может входить в несколько заказов.
#
# Поля модели «Клиент»:
# — имя клиента
# — электронная почта клиента
# — номер телефона клиента
# — адрес клиента
# — дата регистрации клиента
#
# Поля модели «Товар»:
# — название товара
# — описание товара
# — цена товара
# — количество товара
# — дата добавления товара
#
# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказа
#
# Допишите несколько функций CRUD для работы с моделями по желанию.


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
