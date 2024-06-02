# LIBS MODULES
from datetime import datetime
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django.contrib.auth.models import User

from apps.restaurants.serializers import OrderSerializerModel

# SELF MODULES
from .serializers import (
    UsersSerializerModel,
    WaitersSerializerModel,
    WaiterShiftSerializerModel,
)


from .models import Waiter, Waiter_Shift, Tip_Waiter
from apps.restaurants.models import Bill, Order, Restaurant


# Create your views here.
class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializerModel


class WaitersViewSet(ModelViewSet):
    queryset = Waiter.objects.all()
    serializer_class = WaitersSerializerModel
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        waiter = self.get_object()
        print(waiter)
        serialzer = self.get_serializer(waiter)
        now = datetime.now()
        if self.request.query_params.get("extra") == "1":
            waiter_shifts = waiter_shifts = Waiter_Shift.objects.filter(
                Q(waiter=waiter) & Q(start_date__gte=now)
            ).order_by("start_date")[:5]
            shift_serialzer = WaiterShiftSerializerModel(waiter_shifts, many=True)
            return Response(shift_serialzer.data)
        return Response(serialzer.data)

    @action(methods=["post"], detail=True)
    def add_shift(self, request, pk=None):
        waiter = self.get_object()
        waiter_shift_serializer = WaiterShiftSerializerModel(data=request.data)
        if not waiter_shift_serializer.is_valid():
            return Response(waiter_shift_serializer.errors, status=400)
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
        serializer = OrderSerializerModel(orders, many=True)
        if self.request.query_params.get("active") == "1":
            # Lista para almacenar las órdenes activas
            active_orders = []
            for order in orders:
                serializer = OrderSerializerModel(order)
                # Verificar si la orden no tiene una factura asociada
                if not Bill.objects.filter(Q(order=order)).exists():
                    active_orders.append(serializer.data)
                # Verificar si la orden esta asociada a una cuenta pero no tiene un costo final
                elif Bill.objects.filter(Q(order=order) & Q(final_cost=None)).exists():
                    active_orders.append(serializer.data)
            return Response(active_orders)
        return Response(serializer.data)

    @action(methods=["get"], detail=True)
    def get_tips(self, request, pk=None):
        waiter = self.get_object()
        tip_waiter = Tip_Waiter.objects.filter(bill__order__waiter=waiter)
        print(tip_waiter)
        tips_payed = 0
        current_tips = 0
        for tip in tip_waiter:
            if tip.paid:
                tips_payed += (tip.bill.cost * tip.bill.tip_percentage) / 100
            else:
                current_tips += (tip.bill.cost * tip.bill.tip_percentage) / 100
        tips = {
            "tips_payed": tips_payed,
            "Current_tips": current_tips,
        }
        return Response(tips)
