from rest_framework import serializers
from .models import Monitoramento

class MonitoramentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitoramento
        fields = ['id', 'batimentos_por_minuto', 'status']