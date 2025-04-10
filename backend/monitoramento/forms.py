from django import forms
from .models import Medico

class CadastroMedicoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Medico
        fields = ['nome', 'crm', 'email', 'password']