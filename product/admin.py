
from django.contrib import admin

from product.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'gear', 'number_of_seats']
    list_filter = ['category', 'status']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
