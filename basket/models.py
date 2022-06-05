from django.db import models
from django.utils import timezone


class Product(models.Model):
    title = models.CharField('Название товара', max_length=50)
    price = models.PositiveIntegerField('Цена', default=1)
    count = models.PositiveIntegerField('Кол-во товара', default=1)
    made = models.CharField('Название Страны', max_length=50)
    description = models.TextField('Описание')
    img_product = models.ImageField('Фото')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['title']
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        db_table = "product"


class Order(models.Model):
    sum_price = models.PositiveIntegerField('Сумма', default=1)
    date = models.DateTimeField('Дата', default=timezone.now)
    client_name = models.CharField('Имя', max_length=100)
    client_mail = models.EmailField('Почта', max_length=254)

    def __str__(self):
        return f'{self.date} {self.client_name}'

    class Meta:
        ordering = ['date']
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        db_table = "order"


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField('Кол-во товара', default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Номер заказа")

    def __str__(self):
        return f'{self.order}'

    class Meta:
        ordering = ['order']
        verbose_name = "Покупка в корзине"
        verbose_name_plural = "Покупки в корзине"
        db_table = "cart"






# Create your models here.
