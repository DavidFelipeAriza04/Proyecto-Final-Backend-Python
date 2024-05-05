from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.second_name}"


class Waiter(models.Model):
    user = models.ForeignKey("User", on_delete=models.DO_NOTHING)
    OPCIONES_CHOICES = [("MG", "MANAGER"), ("AT", "ADMINTABLES"), ("EX", "EXTRA")]
    charge = models.CharField(max_length=2, choices=OPCIONES_CHOICES, default="EX")

    def __str__(self):
        return f"{self.user.first_name} {self.user.second_name} - {self.get_charge_display()}"


class Waiter_Shift(models.Model):
    waiter = models.ForeignKey("Waiter", on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    restaurant = models.ForeignKey("restaurants.Restaurant", on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.waiter.first_name} {self.waiter.second_name} - {self.shift.date}"


class Tip_Waiter(models.Model):
    bill = models.ForeignKey("restaurants.Bill", on_delete=models.DO_NOTHING)
    waiter = models.ForeignKey("Waiter", on_delete=models.DO_NOTHING)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.waiter.first_name} {self.waiter.second_name} - {self.date}"
