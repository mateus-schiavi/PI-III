from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router.register(r'heartbeats', HeartBeatViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastro_medico, name='cadastro'),
    path('login/', views.login_medico, name='login_medico'),
    path('logout/', views.logout_medico, name='logout_medico'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/monitor_pacientes/', views.salvar_monitoramento, name='salvar_monitoramento'),
    path('dashboard/excluir_agendamento/<int:id>/', views.excluir_agendamento, name='excluir_agendamento')
]

urlpatterns += router.urls
