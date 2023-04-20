from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('category', views.get_category),
    path('product', views.get_product),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
]