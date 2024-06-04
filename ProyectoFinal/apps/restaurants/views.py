# LIBS MODULES
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from django.db.models import Q


# SELF MODULES
from .serializers import (
    OrderDetailSerializerModel,
    RestaurantDetailSerializerModel,
    RestaurantSerializerModel,
    TableSerializerModel,
    OrderSerializerModel,
    BillSerializerModel,
    TablesRestaurantSerializerModel
)

from .models import Restaurant, Table, Order, Bill, Tables_Restaurant

from apps.users.models import Waiter, Waiter_Shift

from .permissions import IsManager, IsManagerOrAdmintables


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
        return Response({"message": "Restaurant deleted successfully"}, status=204)

    def update(self, request, *args, **kwargs):
        restaurant = self.get_object()
        restaurant.name = request.data.get("name", restaurant.name)
        restaurant.address = request.data.get("address", restaurant.address)
        restaurant.owner = request.data.get("owner", restaurant.owner)
        serializer = self.get_serializer(restaurant, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class TablesViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializerModel
    permission_classes = [IsAuthenticated]

    def filter_queryset(self, queryset):
        user = self.request.user
        try:
            waiter = Waiter.objects.get(user=user)
        except Waiter.DoesNotExist:
            return queryset.none()
        now = datetime.now()
        waiter_shifts = Waiter_Shift.objects.filter(
            Q(waiter=waiter) & Q(start_date__lte=now) & Q(end_date__gte=now)
        )
        if waiter_shifts.exists():
            return queryset
        return queryset.none()

    def destroy(self, request, *args, **kwargs):
        table = self.get_object()
        table.delete()
        return Response({"message": "Table deleted successfully"}, status=204)

    def update(self, request, *args, **kwargs):
        table = self.get_object()
        table.number = request.data.get("number", table.number)
        table.person_capacity = request.data.get(
            "person_capacity", table.person_capacity
        )
        serializer = self.get_serializer(table, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class OrdersViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializerModel
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.query_params.get("detail", False):
            return OrderDetailSerializerModel
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action == "destroy":
            return super().get_permissions() + [IsManagerOrAdmintables()]
        return super().get_permissions()
    
    def destroy(self, request, *args, **kwargs):
        order = self.get_object()
        order.delete()
        return Response({"message": "Order deleted successfully"}, status=204)

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        order.waiter = request.data.get("waiter", order.waiter)
        order.table_restaurant = request.data.get(
            "table_restaurant", order.table_restaurant
        )
        serializer = self.get_serializer(order, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class BillsViewSet(ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializerModel
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == "destroy":
            return super().get_permissions() + [IsManager()]
        return super().get_permissions()

    def destroy(self, request, *args, **kwargs):
        bill = self.get_object()
        bill.delete()
        return Response({"message": "Bill deleted successfully"}, status=204)

    def update(self, request, *args, **kwargs):
        bill = self.get_object()
        bill.cost = request.data.get("cost", bill.cost)
        bill.tip_percentage = request.data.get("tip_percentage", bill.tip_percentage)
        bill.final_cost = request.data.get("final_cost", bill.final_cost)
        bill.order = request.data.get("order", bill.order)
        serializer = self.get_serializer(bill, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class TablesRestaurantViewSet(ModelViewSet):
    queryset = Tables_Restaurant.objects.all()
    serializer_class = TablesRestaurantSerializerModel