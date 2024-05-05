from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

#SELF MODULES
from .serializers import UsersSerializerModel, WaitersSerializerModel

from .models import User, Waiter
# Create your views here.
class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializerModel

class WaitersViewSet(ModelViewSet):
    queryset = Waiter.objects.all()
    serializer_class = WaitersSerializerModel