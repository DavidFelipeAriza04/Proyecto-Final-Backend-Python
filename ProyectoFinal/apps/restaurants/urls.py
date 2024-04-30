from django.urls import path, include
from .views import RestaurantsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"restaurants", RestaurantsViewSet, basename="restaurantsViewSet")
urlpatterns = [
    path("", include(router.urls)),
]
