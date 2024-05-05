from rest_framework import serializers
from .models import User, Waiter


class UsersSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class WaitersSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        fields = '__all__'