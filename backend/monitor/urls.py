from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HeartBeatViewSet

router = DefaultRouter()
router.register(r'heartbeat', HeartBeatViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
