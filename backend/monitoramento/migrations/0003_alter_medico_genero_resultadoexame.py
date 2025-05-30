# Generated by Django 5.2 on 2025-05-07 22:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoramento', '0002_medico_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1, null=True),
        ),
        migrations.CreateModel(
            name='ResultadoExame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exame', models.CharField(max_length=100)),
                ('resultado', models.TextField()),
                ('data_exame', models.DateField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resultados_exames', to='monitoramento.monitorpaciente')),
            ],
        ),
    ]
