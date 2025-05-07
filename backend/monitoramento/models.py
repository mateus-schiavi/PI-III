from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class MedicoManager(BaseUserManager):
    def create_user(self, email, nome, crm, password=None):
        if not email:
            raise ValueError("O usuário deve ter um e-mail")
        if not crm:
            raise ValueError("O usuário deve ter um CRM")

        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, crm=crm)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, crm, password=None):
        user = self.create_user(email, nome, crm, password)
        user.is_admin = True  # opcional
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Medico(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    genero = models.CharField(
        max_length=1,
        choices = [('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')],
        blank=False,
        null = True,
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = MedicoManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'crm']

    def __str__(self):
        return self.nome
    
class MonitorPaciente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    data_exame = models.DateField()
    data_consulta = models.DateField()
    observacoes = models.TextField(blank=True, null=True)

    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='pacientes')

    # Alterando o related_name para evitar conflito
    resultados_exames = models.ManyToManyField('ResultadoExame', related_name='exames_do_paciente')

    def __str__(self):
        return self.nome


class ResultadoExame(models.Model):
    paciente = models.ForeignKey(MonitorPaciente, on_delete=models.CASCADE, related_name='resultados_do_paciente')  # Modifique aqui
    exame = models.CharField(max_length=100)
    resultado = models.TextField()
    data_exame = models.DateField()

    def __str__(self):
        return f"Resultado de {self.exame} - {self.paciente.nome}"
    
class HeartBeat(models.Model):
    paciente = models.ForeignKey(MonitorPaciente, on_delete=models.CASCADE, related_name='batimentos_cardiacos', null=True, blank=True)
    bpm = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Batimento de {self.paciente.nome} em {self.timestamp}"
