from django.urls import path
from .views import cadastro_medico, login_medico, logout_medico, HeartBeatViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'heartbeats', HeartBeatViewSet)

urlpatterns = [
    path('cadastrar/', cadastro_medico, name='cadastro'),
    path('login/', login_medico, name='login_medico'),
    path('logout/', logout_medico, name='logout_medico'),
]

urlpatterns += router.urls
