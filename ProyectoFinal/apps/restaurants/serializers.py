# LIBS MODULES
from rest_framework import serializers

# SELF MODULES
from apps.users.models import User
from apps.users.serializers import WaitersSerializerModel
from .models import Restaurant, Table, Order, Bill


class OwnerSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class OrderDetailSerializerModel(serializers.ModelSerializer):
    waiter = WaitersSerializerModel()
    class Meta:
        model = Order
        fields = "__all__"

class RestaurantSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class RestaurantDetailSerializerModel(serializers.ModelSerializer):
    owner = OwnerSerializerModel()

    class Meta:
        model = Restaurant
        fields = "__all__"


class TableSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class OrderSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class BillSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"
