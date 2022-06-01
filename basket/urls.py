from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.ProductListView.as_view(), name='products_list'),
    path('<int:pk>/',views.product_create, name='products_detail'),
    path('cart/',views.CartsListView.as_view(), name='Carts')

]

