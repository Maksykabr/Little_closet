from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'little_closet/index.html', context=context,)


def get_category(request, slug, id):
    categories = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'little_closet/category.html', context=context,)


def get_product(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'product': product,
    }
    return render(request, 'little_closet/product.html', context=context,)


def cart(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'little_closet/cart.html', context=context,)


def checkout(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'little_closet/checkout.html', context=context,)
