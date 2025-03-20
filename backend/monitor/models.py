from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
class HeartBeat(models.Model):
    bpm = models.IntegerField()  # Batimentos por minuto
    timestamp = models.DateTimeField(auto_now_add=True)  # Hora do registro

    def __str__(self):
        return f"{self.bpm} BPM at {self.timestamp}"

class MedicoManager(BaseUserManager):
    def create_user(self, email, nome, crm, password=None):
        if not email:
            raise ValueError("O usuário deve ter um e-mail")
        if not crm:
            raise ValueError("O usuário deve ter um CRM")

        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, crm=crm)
        user.set_password(password)
        user.save(using=self._db)  # Salva corretamente o usuário
        return user

    def create_superuser(self, email, nome, crm, password=None):
        user = self.create_user(email, nome, crm, password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Medico(AbstractBaseUser):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    objects = MedicoManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  ['nome', 'crm']

    def __str__(self):
        return self.nome