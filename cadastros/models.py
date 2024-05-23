from django.db import models

# Create your models here.


class PlanoFinanceiro(models.Model):
    Plano_financeiro = models.CharField(max_length=100)
    Departamento = models.CharField(max_length=100)
    Ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.Plano_financeiro
    

class Usuario(models.Model):

    def get_choices():
        opcoes = PlanoFinanceiro.objects.filter(Ativo=True).values_list('Departamento', flat=True).distinct()
        choices = [(opcao, opcao) for opcao in opcoes]
        return choices

    Usuario = models.CharField(max_length=100)
    Senha_do_usuario = models.CharField(max_length=100)
    Departamento = models.CharField(max_length=100, choices = get_choices)
    Ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.Usuario
 

 