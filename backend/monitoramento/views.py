from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import SetPasswordForm

from .forms import CadastroMedicoForm
from .models import Medico, MonitorPaciente, HeartBeat
from .serializers import HeartBeatSerializer

from rest_framework import viewsets

User = get_user_model()  # usa o modelo Medico como usuário

# ViewSet da API
class HeartBeatViewSet(viewsets.ModelViewSet):
    queryset = HeartBeat.objects.all()
    serializer_class = HeartBeatSerializer

# Página inicial
def home(request):
    return render(request, 'template.html')

# Cadastro de médico
def cadastro_medico(request):
    if request.method == 'POST':
        form = CadastroMedicoForm(request.POST)
        if form.is_valid():
            medico = form.save(commit=False)
            senha = form.cleaned_data['password']
            medico.set_password(senha)
            medico.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login_medico')
    else:
        form = CadastroMedicoForm()

    return render(request, 'cadastro.html', {'form': form})

# Login
@csrf_protect
def login_medico(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Credenciais inválidas.')

    return render(request, 'login.html')

# Dashboard (após login)
@never_cache
@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'dashboard.html')

# Logout
def logout_medico(request):
    logout(request)
    return redirect('login_medico')

# Redefinir senha
def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')

        medico = User.objects.filter(email__iexact=email).first()

        if medico:
            form = SetPasswordForm(medico, {'new_password1': new_password, 'new_password2': new_password})
            if form.is_valid():
                form.save()
                messages.success(request, 'Sua senha foi redefinida com sucesso!')
                return redirect('login_medico')
            else:
                for error in form.errors.values():
                    messages.error(request, error)
        else:
            messages.error(request, 'Nenhum usuário encontrado com esse e-mail')

    return render(request, 'reset_password.html')

# Monitoramento de pacientes
@login_required
def salvar_monitoramento(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        data_exame = request.POST.get('data_exame')
        data_consulta = request.POST.get('data_consulta')
        observacoes = request.POST.get('observacoes')

        MonitorPaciente.objects.create(
            nome=nome,
            telefone=telefone,
            data_exame=data_exame,
            data_consulta=data_consulta,
            observacoes=observacoes,
            medico=request.user
        )

        messages.success(request, 'Monitoramento salvo com sucesso!')
        return redirect('salvar_monitoramento')

    agendamentos = MonitorPaciente.objects.filter(medico=request.user).order_by('data_consulta', 'data_exame')
    return render(request, 'monitor_pacientes.html', {'agendamentos': agendamentos})

# Excluir agendamento
@login_required
def excluir_agendamento(request, id):
    agendamento = get_object_or_404(MonitorPaciente, id=id)
    agendamento.delete()
    messages.success(request, 'Agendamento excluído com sucesso!')
    return redirect('salvar_monitoramento')
