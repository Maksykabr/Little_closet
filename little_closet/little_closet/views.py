from django.shortcuts import render
from .models import Category, Product, Image


def index(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'little_closet/index.html', context=context,)


def get_category(request, slug, id):
    categories = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    context = {
        'categories': categories,
    }
    return render(request, 'little_closet/category.html', context=context,)


def get_product(request, id, slug):
    return render(request, 'little_closet/product.html')


def cart(request):
    return render(request, 'little_closet/cart.html')


def checkout(request):
    return render(request, 'little_closet/checkout.html')
