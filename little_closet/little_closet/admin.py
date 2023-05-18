from django.contrib import admin
from .models import Category, Product
from django.utils.safestring import mark_safe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'price', 'available', 'created_at', 'category', 'get_image']

    readonly_fields = ("get_image",)

    def get_image(self, obj):
        if obj.image:
            return mark_safe("<img src = '{}' width = '60' />".format(obj.image.url))

    list_filter = ['available', 'created_at']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}



