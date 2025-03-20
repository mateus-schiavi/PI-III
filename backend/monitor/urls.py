from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router.register(r'heartbeats', HeartBeatViewSet)

urlpatterns = [
    path('cadastrar/', views.cadastro_medico, name='cadastro'),
    path('login/', views.login_medico, name='login_medico'),
    path('logout/', views.logout_medico, name='logout_medico'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

urlpatterns += router.urls
