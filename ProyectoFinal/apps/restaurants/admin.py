# LIBS IMPORTS
from django.contrib import admin

# SELF IMPORTS
from .models import (
    Bill,
    Table,
    Order,
    Product,
    Products_Order,
    Products_Restaurant,
    Restaurant,
    Tables_Restaurant,
    Tip_Waiter,
    Waiter,
    Waiter_Shift,
)


# Register your models here.


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["id","name", "address", "owner"]


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "cost_per_unit", "all_restaurants"]


class Products_RestaurantAdmin(admin.ModelAdmin):
    list_display = ["product", "restaurant"]


class TableAdmin(admin.ModelAdmin):
    list_display = ["number", "person_capacity"]


class Tables_RestaurantAdmin(admin.ModelAdmin):
    list_display = ["table", "restaurant"]


class WaiterAdmin(admin.ModelAdmin):
    list_display = ["user", "charge"]


class Waiter_ShiftAdmin(admin.ModelAdmin):
    list_display = ["waiter", "start_date", "end_date", "restaurant"]


class Tip_WaiterAdmin(admin.ModelAdmin):
    list_display = ["bill", "waiter", "paid"]


class BillAdmin(admin.ModelAdmin):
    list_display = ["order", "cost", "tip_percentage", "final_cost"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["waiter", "table_restaurant"]


class Products_OrderAdmin(admin.ModelAdmin):
    list_display = ["product", "order"]


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Products_Restaurant, Products_RestaurantAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Tables_Restaurant, Tables_RestaurantAdmin)
admin.site.register(Waiter, WaiterAdmin)
admin.site.register(Waiter_Shift, Waiter_ShiftAdmin)
admin.site.register(Tip_Waiter, Tip_WaiterAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Products_Order, Products_OrderAdmin)
