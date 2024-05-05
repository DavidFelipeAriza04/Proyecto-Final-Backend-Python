from django.urls import path, include
from .views import ProductsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"products", ProductsViewSet, basename="products")
urlpatterns = [
    path("", include(router.urls)),
]
