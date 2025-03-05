from django.urls import path
from .views import MonitoramentoList, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path ('api/monitoramento/', MonitoramentoList.as_view(), name='monitoramento-list')
 ]