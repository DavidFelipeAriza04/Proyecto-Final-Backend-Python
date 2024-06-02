from rest_framework import serializers
from .models import Waiter, Waiter_Shift, Tip_Waiter
from django.contrib.auth.models import User

class UsersSerializerModel(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "password"]
    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = User(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user

class WaitersSerializerModel(serializers.ModelSerializer):
    # user = UsersSerializerModel()
    class Meta:
        model = Waiter
        fields = "__all__"

class WaiterShiftSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Waiter_Shift
        fields = "id","start_date", "end_date", "restaurant"

class Tip_WaiterSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Tip_Waiter
        fields = "__all__"