from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import ListView, DetailView
import logging
from .models import *


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


logger = logging.getLogger('main')


def product_create(request):
    products = Product.objects.all()
    info = ''
    s_price = 0
    client_mail = ''
    name = ''
    product_dict = {}
    if request.method == 'POST':
        zakaz = Order(sum_price=s_price, client_mail=client_mail, client_name=name)
        zakaz.save()
        temp = request.POST
        logger.info(temp)
        # logger.error('dada')
        for k, v in temp.items():
            try:
                id_pro = int(k)
                count_p = int(v)
            except:
                continue
            name = temp['name']
            client_mail = temp['email']
            if count_p > 0:
                product = Product.objects.get(id=id_pro)
                product_dict[str(product.title)] = count_p
                price = product.price * count_p
                s_price += price
                product.count -= count_p
                Cart.objects.create(product_id=id_pro, count=count_p,  order_id=zakaz.pk)
                product.save()
                if s_price > 0:
                    info = f'Здравствуйте, {name}, вы заказали: {unpack(product_dict)} Сумма вашего заказа: {s_price}руб. , ' \
                       f'номер вашего заказа: {zakaz.pk}'
                else:
                    info = f'Ошибка в заказе'
        zakaz_edit = Order.objects.get(id=zakaz.pk)
        zakaz_edit.sum_price = s_price
        zakaz_edit.client_mail = client_mail
        zakaz_edit.client_name = name
        zakaz_edit.save()
    send_mail(
        subject='order',
        message=info,
        from_email='ilushamdmaa@yandex.ru',
        recipient_list=[client_mail],
    )

    return render(request, 'products.html', {'products': products, 'info': info})


class OrdersListView(ListView):
    model = Order
    template_name = 'Orders.html'


def order_show(request,pk):
    orders = Cart.objects.filter(order_id=pk)
    return render(request,'order_detail.html', {'orders': orders})

def unpack(s):
    res = ''
    for k, v in s.items():
        res += f' {k} - {v},'
    return res[:-1] + '.'


    # print(request.POST)
    # if request.method == 'POST':
    #     print(request.POST)
    #     data = Product.objects.all()
    #     id_p = dict_products(data)
    #     row = Product.objects.get(id=id_p[request.POST['name']])
    #     temp = Cart(product_id=id_p[request.POST['name']],count=request.POST['count'])
    #     temp.save()
    #     amount = int(request.POST['count'])
    #     row.count -= amount
    #     row.save()
    #     temp.save()
    # products = Product.objects.all()
    # cart = Cart.objects.all()
    # count_product = [i.count for i in products]
    # title_products = [i for i in products]
    # return render(request,'products.html', {'products':products,'count_product': count_product,
    #                                         'title_products': title_products,'cart':cart})
# Create your views here.

# def dict_products(data):
#     data = Product.objects.all()
#     data_name = [i.title for i in data]
#     data_id = [str(i.id) for i in data]
#     data_name_id = dict(zip(data_name,data_id))
#     return data_name_id



# for pro_id in request.POST:
#     try:
#         int(pro_id)
#     except:
#         continue
#     if int(request.POST[pro_id]) > 0:
#         temp = Cart(product_id=request.POST[pro_id], count=pro_id, client_name='ilya', sum_price=3000)
#         temp.save()
# if int(request.POST['count']) > 0 and int(request.POST['count']) <= product_count:
#     temp = Cart(product_id=pk,count=request.POST['count'],client_name=request.POST['name'],
#                 sum_price=int(request.POST["count"])*product.price)
#     product.count -= int(request.POST['count'])
#     product.save()
#     temp.save()
#     info = f'{request.POST["name"]}, ваш заказ оформлен на сумму {int(request.POST["count"])*product.price} руб.'
#     print(request.POST)
# else:
#     if int(request.POST['count']) > product_count:
#         info = 'Кол-во не может быть больше чем товара на складе'
#     else:
#         info = 'Кол-во не может меньше 1'