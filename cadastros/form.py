from .models import PlanoFinanceiro, Usuario
from django import forms


class PlanofinanceiroForm(forms.ModelForm):
    class Meta:
        model = PlanoFinanceiro
        fields = ['Plano_financeiro', 'Departamento']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['Usuario', 'Senha_do_usuario', 'Departamento']





