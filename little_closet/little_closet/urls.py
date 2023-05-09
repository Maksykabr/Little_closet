from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<slug:slug>/<int:id>', views.get_category, name='get_category'),
    path('product', views.get_product),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
]