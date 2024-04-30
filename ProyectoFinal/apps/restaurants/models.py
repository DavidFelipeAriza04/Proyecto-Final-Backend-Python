from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    owner = models.ForeignKey("users.User", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    cost_per_unit = models.FloatField()
    all_restaurants = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.name


class Products_Restaurant(models.Model):
    product = models.ForeignKey("Product", on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey("Restaurant", on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.product.name} - {self.restaurant.name}"


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


class Waiter(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.DO_NOTHING)
    charge = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.second_name}"


class Waiter_Shift(models.Model):
    waiter = models.ForeignKey("Waiter", on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    restaurant = models.ForeignKey("Restaurant", on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.waiter.first_name} {self.waiter.second_name} - {self.shift.date}"


class Tip_Waiter(models.Model):
    bill = models.ForeignKey("Bill", on_delete=models.DO_NOTHING)
    waiter = models.ForeignKey("Waiter", on_delete=models.DO_NOTHING)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.waiter.first_name} {self.waiter.second_name} - {self.date}"


class Bill(models.Model):
    order = models.ForeignKey("Order", on_delete=models.DO_NOTHING)
    cost = models.FloatField()
    tip_percentage = models.FloatField()
    final_cost = models.FloatField()

    def __str__(self):
        return f"{self.order} - {self.cost}"


class Order(models.Model):
    waiter = models.ForeignKey("Waiter", on_delete=models.DO_NOTHING)
    table_restaurant = models.ForeignKey(
        "Tables_Restaurant", on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return f"{self.waiter.first_name} {self.waiter.second_name} - {self.date}"


class Products_Order(models.Model):
    product = models.ForeignKey("Product", on_delete=models.DO_NOTHING)
    order = models.ForeignKey("Order", on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.product.name} - {self.order}"
