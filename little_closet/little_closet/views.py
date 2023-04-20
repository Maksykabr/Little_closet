from django.shortcuts import render


def index(request):
    return render(request, 'little_closet/index.html')


def get_category(request):
    return render(request, 'little_closet/category.html')


def get_product(request):
    return render(request, 'little_closet/product.html')


def cart(request):
    return render(request, 'little_closet/cart.html')


def checkout(request):
    return render(request, 'little_closet/checkout.html')
