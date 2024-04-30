from rest_framework import serializers

from apps.users.models import User


from .models import Restaurant


class OwnerSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = User
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
