from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  # Adicionando o módulo de mensagens
from .forms import CadastroMedicoForm
from .models import Medico
from rest_framework import viewsets
from .models import HeartBeat
from .serializers import HeartBeatSerializer
from django.http import HttpResponse
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User
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

            # Adicionando a mensagem de sucesso
            messages.success(request, 'Cadastro realizado com sucesso! Agora, faça o seu login.')

            return redirect('login_medico')  # Redireciona para a página de login
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
    return redirect('login_medico')

def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')

        try:
            user = User.objects.get(email=email)
            form = SetPasswordForm(user, {'new_password1': new_password, 'new_password2': new_password})

            if form.is_valid():
                form.save()
                messages.success(request, 'Sua senha foi redefinida com sucesso!')
                return redirect('login_medico')
            else:
                messages.error(request, 'Houve um erro ao tentar redefinir a senha.')
        except User.DoesNotExist:
            messages.error(request, 'Nenhum usuário encontrado com esse e-mail')

    return render(request, 'reset_password.html')

