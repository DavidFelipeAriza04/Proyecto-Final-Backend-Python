from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


# Create your models here.
class Waiter(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    OPCIONES_CHOICES = [("MG", "MANAGER"), ("AT", "ADMINTABLES"), ("EX", "EXTRA")]
    charge = models.CharField(max_length=2, choices=OPCIONES_CHOICES, default="EX")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.get_charge_display()}"


class Waiter_Shift(models.Model):
    waiter = models.ForeignKey("Waiter", on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    restaurant = models.ForeignKey("restaurants.Restaurant", on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.waiter.user.first_name} {self.waiter.user.last_name} - {self.start_date} - {self.end_date}"


class Tip_Waiter(models.Model):
    bill = models.ForeignKey("restaurants.Bill", on_delete=models.DO_NOTHING)
    waiter = models.ForeignKey("Waiter", on_delete=models.DO_NOTHING)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.waiter.first_name} {self.waiter.last_name} - {self.date}"
