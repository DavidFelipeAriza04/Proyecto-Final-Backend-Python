# LIBS MODULES
from rest_framework import serializers

# SELF MODULES
from .models import Product, Products_Restaurant, Products_Order


class ProductSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductsRestaurantSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Products_Restaurant
        fields = "__all__"


class ProductsOrderSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Products_Order
        fields = "__all__"
