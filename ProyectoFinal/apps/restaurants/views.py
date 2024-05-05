from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

#SELF MODULES
from .serializers import RestaurantDetailSerializerModel, RestaurantSerializerModel, TableSerializerModel, OrderSerializerModel, BillSerializerModel

from .models import Restaurant, Table, Order, Bill
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

    def update(self, request, *args, **kwargs):
        restaurant = self.get_object()
        restaurant.name = request.data.get('name', restaurant.name)
        restaurant.address = request.data.get('address', restaurant.address)
        restaurant.owner = request.data.get('owner', restaurant.owner)
        serializer = self.get_serializer(restaurant, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class TablesViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializerModel
    
    def destroy(self, request, *args, **kwargs):
        table = self.get_object()
        table.delete()
        return Response({'message': 'Table deleted successfully'}, status=204)
    
    def update(self, request, *args, **kwargs):
        table = self.get_object()
        table.number = request.data.get('number', table.number)
        table.person_capacity = request.data.get('person_capacity', table.person_capacity)
        serializer = self.get_serializer(table, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class OrdersViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializerModel
    
    def destroy(self, request, *args, **kwargs):
        order = self.get_object()
        order.delete()
        return Response({'message': 'Order deleted successfully'}, status=204)
    
    def update(self, request, *args, **kwargs):
        order = self.get_object()
        order.waiter = request.data.get('waiter', order.waiter)
        order.table_restaurant = request.data.get('table_restaurant', order.table_restaurant)
        serializer = self.get_serializer(order, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class BillsViewSet(ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializerModel