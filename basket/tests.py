from django.test import TestCase, Client
from django.urls import reverse
from .models import *


class MyTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        product = Product.objects.create(title="Мышка", count=30, price=5000)
        product = Product.objects.create(title="Наушники", count=17, price=10000)


    def setUp(self):
        prod = Product.objects.all()[0]
        amount = 4
        price_sum = 3400
        dic_post = {str(prod.id): str(amount),
                   'name':'ilya',
                   'email':'test@yandex.ru'}
        self.client = Client()
        self.client.post(f'/products/', dic_post)
        zakaz = Order(sum_price=price_sum, client_mail=dic_post['email'], client_name=dic_post['name'])
        zakaz.save()

    def test_get_product(self):
        prod = Product.objects.get(pk=2)
        self.assertEqual(prod.title, 'Наушники')

    def test_view_url(self):
        resp = self.client.get('/products/orders/')
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('Orders'))
        self.assertTemplateUsed(resp, 'Orders.html')

    def test_get_product_count_change_after_purchase(self):
        prod = Product.objects.all()[0]
        self.assertEqual(prod.count, 26)

    def test_get_cart_count(self):
        cart = Cart.objects.get(pk=1)
        self.assertEqual(cart.count, 4)






