from rest_framework import serializers
from .models import HeartBeat

class HeartBeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeartBeat
        fields = ['id', 'bpm', 'timestamp']
