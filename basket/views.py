from django.shortcuts import render
from .models import *
from django.views.generic import ListView,DetailView

class ProductListView(ListView):
    model = Product
    template_name = 'products.html'

def product_create(request,pk):
    products = Product.objects.filter(id=pk)
    product = Product.objects.get(id=pk)
    product_count = product.count

    info = ''
    # if request.method == "POST":
    #     temp = json.load(request)
    #     print(temp)
    #     res = GameInfo(product_id=pk,count=temp['count'], client_name=temp['name'])
    #     res.save()
    #     now = datetime.now()
    #     return HttpResponse(now.strftime("%Y-%b-%d %H:%M:%S"))
    if request.method == 'POST':
        if int(request.POST['count']) > 0 and int(request.POST['count']) <= product_count:
            temp = Cart(product_id=pk,count=request.POST['count'],client_name=request.POST['name'],
                        sum_price=int(request.POST["count"])*product.price)
            product.count -= int(request.POST['count'])
            product.save()
            temp.save()
            info = f'{request.POST["name"]}, ваш заказ оформлен на сумму {int(request.POST["count"])*product.price} руб.'
            print(request.POST)
        else:
            if int(request.POST['count']) > product_count:
                info = 'Кол-во не может быть больше чем товара на складе'
            else:
                info = 'Кол-во не может меньше 1'

    return render(request, 'product_detail.html', {'products': products,'info': info})

class CartsListView(ListView):
    model = Cart
    template_name = 'Carts.html'
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

