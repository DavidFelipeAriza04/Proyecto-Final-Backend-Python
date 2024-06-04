from django.urls import path, include
from .views import RestaurantsViewSet, TablesViewSet, OrdersViewSet, BillsViewSet,TablesRestaurantViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"tables", TablesViewSet, basename="tables")
router.register(r"tables_restaurant", TablesRestaurantViewSet, basename="tables_restaurant")
router.register(r"restaurants", RestaurantsViewSet, basename="restaurants")
router.register(r"orders", OrdersViewSet, basename="orders")
router.register(r"bills", BillsViewSet, basename="bills")
urlpatterns = [
    path("", include(router.urls)),
]
