from django.contrib import admin


# Register your models here.
from .models import *

class CustomersAdmin(admin.ModelAdmin):
    list_display = ['customer', 'avatar', 'description']


admin.site.register(Customers, CustomersAdmin)


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'cover']

admin.site.register(Products, ProductsAdmin)


class OrderAppAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    list_display = ['title', 'customer', 'product', 'created_at']

admin.site.register(OrderApp, OrderAppAdmin)

