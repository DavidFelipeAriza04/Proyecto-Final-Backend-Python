from rest_framework import serializers
from .models import User, Waiter


class UsersSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "second_name", "email"]


class WaitersSerializerModel(serializers.ModelSerializer):
    # user = UsersSerializerModel()
    class Meta:
        model = Waiter
        fields = "__all__"
