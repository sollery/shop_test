from django.db import models
from django.utils import timezone




class Product(models.Model):
    title = models.CharField('Название товара',max_length=50)
    price = models.PositiveIntegerField('Цена',default=1)
    count = models.PositiveIntegerField('Кол-во товара', default=1)


    def __str__(self):
        return f'{self.title}'


class Cart(models.Model):
    date = models.DateTimeField('Дата', default=timezone.now)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField('Кол-во товара', default=1)
    client_name = models.CharField('Имя', max_length=50)
    sum_price = models.PositiveIntegerField('Сумма',default=1)






# Create your models here.
