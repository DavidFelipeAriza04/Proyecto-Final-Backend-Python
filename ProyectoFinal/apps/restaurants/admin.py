# LIBS IMPORTS
from django.contrib import admin

# SELF IMPORTS
from .models import (
    Bill,
    Table,
    Order,
    Restaurant,
    Tables_Restaurant,
)


# Register your models here.


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "address", "owner"]


class TableAdmin(admin.ModelAdmin):
    list_display = ["number", "person_capacity"]


class Tables_RestaurantAdmin(admin.ModelAdmin):
    list_display = ["table", "restaurant"]


class BillAdmin(admin.ModelAdmin):
    list_display = ["order", "cost", "tip_percentage", "final_cost"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["waiter", "table_restaurant"]





admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Tables_Restaurant, Tables_RestaurantAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(Order, OrderAdmin)

