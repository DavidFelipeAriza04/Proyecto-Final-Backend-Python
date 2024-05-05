from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    cost_per_unit = models.FloatField()
    all_restaurants = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.name


class Products_Restaurant(models.Model):
    product = models.ForeignKey("Product", on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey("restaurants.Restaurant", on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.product.name} - {self.restaurant.name}"


class Products_Order(models.Model):
    product = models.ForeignKey("Product", on_delete=models.DO_NOTHING)
    order = models.ForeignKey("restaurants.Order", on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.product.name} - {self.order}"
