from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CadastroMedicoForm
from .models import Medico
from rest_framework import viewsets
from .models import HeartBeat
from .serializers import HeartBeatSerializer
from django.http import HttpResponse
class HeartBeatViewSet(viewsets.ModelViewSet):
    queryset = HeartBeat.objects.all()
    serializer_class = HeartBeatSerializer

def home(request):
    return render(request, 'template.html')

def cadastro_medico(request):
    if request.method == 'POST':
        form = CadastroMedicoForm(request.POST)
        if form.is_valid():
            medico = form.save(commit=False)
            medico.set_password(form.cleaned_data['password'])
            medico.save()
            return redirect('login')
    else:
        form = CadastroMedicoForm()
    return render(request, 'cadastro.html', {'form': form})

# Página de Login
def login_medico(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redireciona para a área do médico
        else:
            return render(request, 'login.html', {'erro': 'Credenciais inválidas'})

    return render(request, 'login.html')

# Página de Logout
def logout_medico(request):
    logout(request)
    return redirect('login')