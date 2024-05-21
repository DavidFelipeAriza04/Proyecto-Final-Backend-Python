# LIBS MODULES
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django.contrib.auth.models import User

# SELF MODULES
from .serializers import UsersSerializerModel, WaitersSerializerModel


from .models import Waiter, Waiter_Shift
from apps.restaurants.models import Bill, Order, Restaurant


# Create your views here.
class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializerModel


class WaitersViewSet(ModelViewSet):
    queryset = Waiter.objects.all()
    serializer_class = WaitersSerializerModel
    permission_classes = [IsAuthenticated]

    @action(methods=["post"], detail=True)
    def add_shift(self, request, pk=None):
        waiter = self.get_object()
        waiter_shift = Waiter_Shift()
        waiter_shift.waiter = waiter
        waiter_shift.start_date = request.data.get("start_date")
        waiter_shift.end_date = request.data.get("end_date")
        waiter_shift.restaurant = Restaurant.objects.get(
            id=request.data.get("restaurant")
        )
        waiter_shift.save()
        return Response({"message": "Shift added"})

    @action(methods=["get"], detail=True)
    def orders(self, request, pk=None):
        user = self.request.user
        waiter = self.get_object()

        if waiter.user != user:
            return Response({"message": "You are not the waiter"}, status=403)
        orders = Order.objects.filter(waiter=waiter)
        print(orders)
        if self.request.query_params.get("active") == "1":
            # Lista para almacenar las órdenes activas
            active_orders = []
            for order in orders:
                print(order)
                # Verificar si la orden no tiene una factura asociada
                if not Bill.objects.filter(Q(order=order)).exists():
                    active_orders.append(order)
                # Verificar si la orden esta asociada a una cuenta pero no tiene un costo final
                elif Bill.objects.filter(Q(order=order) & Q(final_cost = None)).exists():
                    active_orders.append(order)
            # Serializar las órdenes activas
            active_orders_data = [
                {
                    "id": order.id,
                    "table_restaurant": order.table_restaurant.id,
                    "waiter": order.waiter.id,
                }
                for order in active_orders
            ]
            return Response(active_orders_data)
        return Response(orders.values())
