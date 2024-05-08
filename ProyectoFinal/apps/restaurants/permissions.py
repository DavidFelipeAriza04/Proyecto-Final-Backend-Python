from rest_framework.permissions import BasePermission

from apps.users.models import Waiter


class IsManager(BasePermission):
    def has_permission(self, request, view):
        waiter = Waiter.objects.filter(user=request.user)
        if waiter.exists():
            waiter = waiter.first()
            return waiter.charge == "MG"
        return False

class IsManagerOrAdmintables(BasePermission):
    def has_permission(self, request, view):
        waiter = Waiter.objects.filter(user=request.user)
        if waiter.exists():
            waiter = waiter.first()
            return waiter.charge == "MG" or waiter.charge == "AT"
        return False