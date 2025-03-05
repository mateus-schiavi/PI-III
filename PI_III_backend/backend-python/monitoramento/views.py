from django.views.generic import TemplateView
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Monitoramento
from .serializers import MonitoramentoSerializer
# Create your views here.

class MonitoramentoList(APIView):
    def get(self, request):
        monitoramentos = Monitoramento.objects.all()
        serializer = MonitoramentoSerializer(monitoramentos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MonitoramentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HomeView(TemplateView):
    template_name = 'home.html'