from django.db import models

# Create your models here.
class Monitoramento(models.Model):
    batimentos_por_minutos = models.IntegerField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return f'Batimentos: {self.batimentos_por_minutos}, Status: {self.status}'
        