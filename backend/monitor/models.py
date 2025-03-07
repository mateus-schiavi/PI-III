from django.db import models

class HeartBeat(models.Model):
    bpm = models.IntegerField()  # Batimentos por minuto
    timestamp = models.DateTimeField(auto_now_add=True)  # Hora do registro

    def __str__(self):
        return f"{self.bpm} BPM at {self.timestamp}"
