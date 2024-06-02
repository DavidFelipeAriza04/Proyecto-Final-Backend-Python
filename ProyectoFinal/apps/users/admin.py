# LIBS IMPORTS
from django.contrib import admin

# SELF IMPORTS
from .models import Waiter, Waiter_Shift, Tip_Waiter

class WaiterAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "charge"]


class Waiter_ShiftAdmin(admin.ModelAdmin):
    list_display = ["id", "waiter", "start_date", "end_date", "restaurant"]


class Tip_WaiterAdmin(admin.ModelAdmin):
    list_display = ["id", "bill", "waiter", "paid"]


admin.site.register(Waiter, WaiterAdmin)
admin.site.register(Waiter_Shift, Waiter_ShiftAdmin)
admin.site.register(Tip_Waiter, Tip_WaiterAdmin)
