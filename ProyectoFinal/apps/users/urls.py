from django.urls import path, include
from .views import UsersViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"users", UsersViewSet, basename="usersViewSet")
urlpatterns = [
    path("", include(router.urls)),
]