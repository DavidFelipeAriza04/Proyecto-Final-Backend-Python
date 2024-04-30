from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

#SELF MODULES
from .serializers import UsersSerializerModel

from .models import User
# Create your views here.
class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializerModel