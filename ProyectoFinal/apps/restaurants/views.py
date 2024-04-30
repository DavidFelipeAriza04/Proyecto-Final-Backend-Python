from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

#SELF MODULES
from .serializers import RestaurantDetailSerializerModel, RestaurantSerializerModel

from .models import Restaurant
# Create your views here.
class RestaurantsViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializerModel
    
    def get_serializer_class(self):
        if self.request.query_params.get("detail", False):
            return RestaurantDetailSerializerModel
        return super().get_serializer_class()
    
    def destroy(self, request, *args, **kwargs):
        restaurant = self.get_object()
        restaurant.delete()
        return Response({'message': 'Restaurant deleted successfully'}, status=204)