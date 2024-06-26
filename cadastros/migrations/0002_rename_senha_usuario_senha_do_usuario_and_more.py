# Generated by Django 5.0.3 on 2024-05-06 19:06

import cadastros.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='Senha',
            new_name='Senha_do_usuario',
        ),
        migrations.AddField(
            model_name='planofinanceiro',
            name='Ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='Ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='Departamento',
            field=models.CharField(choices=cadastros.models.Usuario.get_choices, default='abc', max_length=100),
        ),
    ]
