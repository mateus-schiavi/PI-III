from django.contrib import admin
from django.urls import path, include
from monitor.views import home  # Importar a view home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Define a rota da página inicial
    path('', include('monitor.urls')),  # Inclui as URLs do app monitor
]
