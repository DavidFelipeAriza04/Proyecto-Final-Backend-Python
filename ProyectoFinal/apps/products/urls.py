from django.urls import path, include
from .views import ProductsViewSet, ProductsRestaurantViewSet, ProductsOrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"products", ProductsViewSet, basename="products")
router.register(r"products_restaurant", ProductsRestaurantViewSet, basename="products_restaurant")
router.register(r"products_order", ProductsOrderViewSet, basename="products_order")
urlpatterns = [
    path("", include(router.urls)),
]
