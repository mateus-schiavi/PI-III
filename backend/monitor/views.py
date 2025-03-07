from django.shortcuts import render
from rest_framework import viewsets
from .models import HeartBeat
from .serializers import HeartBeatSerializer
from django.http import HttpResponse
class HeartBeatViewSet(viewsets.ModelViewSet):
    queryset = HeartBeat.objects.all()
    serializer_class = HeartBeatSerializer

def home(request):
    return HttpResponse("Bem-vindo à página inicial da API!")