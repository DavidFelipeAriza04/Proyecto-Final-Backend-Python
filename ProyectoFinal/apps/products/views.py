from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

#SELF MODULES
from .serializers import ProductSerializerModel, ProductsRestaurantSerializerModel, ProductsOrderSerializerModel

from .models import Product, Products_Restaurant, Products_Order
# Create your views here.
class ProductsViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerModel
    
    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        product.delete()
        return Response({'message': 'Product deleted successfully'}, status=204)

    def update(self, request, *args, **kwargs):
        product = self.get_object()
        product.name = request.data.get('name', product.name)
        product.cost_per_unit = request.data.get('cost_per_unit', product.cost_per_unit)
        product.all_restaurants = request.data.get('all_restaurants', product.all_restaurants)
        serializer = self.get_serializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class ProductsRestaurantViewSet(ModelViewSet):
    queryset = Products_Restaurant.objects.all()
    serializer_class = ProductsRestaurantSerializerModel

class ProductsOrderViewSet(ModelViewSet):
    queryset = Products_Order.objects.all()
    serializer_class = ProductsOrderSerializerModel