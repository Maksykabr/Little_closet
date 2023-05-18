from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('category/<slug:slug>/<int:id>', views.get_category, name='get_category'),
    path('product/<slug:slug>/<int:id>', views.get_product, name='get_product'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
]