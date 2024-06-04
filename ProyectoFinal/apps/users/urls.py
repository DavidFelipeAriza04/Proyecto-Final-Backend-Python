from django.urls import path, include
from .views import UsersViewSet, WaitersViewSet, TipWaiterViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r"waiters", WaitersViewSet, basename="waiters")
router.register(r"users", UsersViewSet, basename="users")
router.register(r"tip_waiter", TipWaiterViewSet, basename="tip_waiter")
urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
