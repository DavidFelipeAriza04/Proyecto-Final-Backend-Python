# LIBS IMPORTS
from django.contrib import admin

# SELF IMPORTS
from .models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["id","first_name", "second_name", "email"]


admin.site.register(User, UserAdmin)
