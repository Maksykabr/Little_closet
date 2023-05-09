from django.contrib import admin
from .models import Category, Product, Image
from django.utils.safestring import mark_safe


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Image)

