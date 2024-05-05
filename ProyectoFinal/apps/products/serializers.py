#LIBS MODULES
from rest_framework import serializers

#SELF MODULES
from apps.users.models import User
from .models import Product

class ProductSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'