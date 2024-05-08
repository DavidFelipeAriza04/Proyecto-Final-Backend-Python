from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    owner = models.ForeignKey("users.User", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Table(models.Model):
    number = models.IntegerField()
    person_capacity = models.IntegerField()

    def __str__(self):
        return f"{self.number}"


class Tables_Restaurant(models.Model):
    table = models.ForeignKey("Table", on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey("Restaurant", on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.table.number} - {self.restaurant.name}"


class Bill(models.Model):
    order = models.ForeignKey("Order", on_delete=models.DO_NOTHING)
    cost = models.FloatField()
    tip_percentage = models.FloatField()
    final_cost = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.order} - {self.cost}"


class Order(models.Model):
    waiter = models.ForeignKey("users.Waiter", on_delete=models.DO_NOTHING)
    table_restaurant = models.ForeignKey(
        "Tables_Restaurant", on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return f"{self.waiter.user.first_name} {self.waiter.user.second_name} - {self.table_restaurant.table.number} {self.table_restaurant.restaurant.name}"

