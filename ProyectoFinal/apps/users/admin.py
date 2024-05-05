# LIBS IMPORTS
from django.contrib import admin

# SELF IMPORTS
from .models import User, Waiter, Waiter_Shift, Tip_Waiter


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["id","first_name", "second_name", "email"]


class WaiterAdmin(admin.ModelAdmin):
    list_display = ["user", "charge"]


class Waiter_ShiftAdmin(admin.ModelAdmin):
    list_display = ["waiter", "start_date", "end_date", "restaurant"]


class Tip_WaiterAdmin(admin.ModelAdmin):
    list_display = ["bill", "waiter", "paid"]


admin.site.register(User, UserAdmin)
admin.site.register(Waiter, WaiterAdmin)
admin.site.register(Waiter_Shift, Waiter_ShiftAdmin)
admin.site.register(Tip_Waiter, Tip_WaiterAdmin)
