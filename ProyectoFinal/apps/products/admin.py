from django.contrib import admin

from .models import Product, Products_Restaurant, Products_Order


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "cost_per_unit", "all_restaurants"]


class Products_RestaurantAdmin(admin.ModelAdmin):
    list_display = ["product", "restaurant"]


class Products_OrderAdmin(admin.ModelAdmin):
    list_display = ["product", "order"]


admin.site.register(Products_Order, Products_OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Products_Restaurant, Products_RestaurantAdmin)
