from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.product_create, name='products_list'),
    path('<int:pk>/',views.ProductDetailView.as_view(), name='products_detail'),
    path('orders/',views.OrdersListView.as_view(), name='Orders'),
    path('order/<int:pk>/',views.order_show, name='order_detail'),


]

