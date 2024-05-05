from django.urls import path, include
from .views import UsersViewSet, WaitersViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"waiters", WaitersViewSet, basename="waiters")
router.register(r"users", UsersViewSet, basename="users")
urlpatterns = [
    path("", include(router.urls)),
]