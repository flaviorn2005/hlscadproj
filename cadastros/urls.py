from django.urls import path
from . import views

urlpatterns = [
    path('', views.tipo_cadastro, name='tipo_cadastro'),
    path('cadastro_planofinanceiro/', views.cadastro_planofinanceiro, name='cadastro_planofinanceiro'),
    path('cadastro_usuario/', views.cadastro_usuario, name='cadastro_usuario'),
    path('todos_planosfinanceiros/', views.todos_planosfinaceiros, name='todos_planosfinanceiros'),
    path('atualiza_planosfinanceiros/<int:pk>/', views.atualiza_planosfinanceiros, name='atualiza_planosfinanceiros'),
    path('exclui_planosfinanceiros/<int:pk>/', views.exclui_planosfinanceiros, name='exclui_planosfinanceiros'),
    path('todos_usuarios/', views.todos_usuarios, name='todos_usuarios'),
    path('atualiza_usuarios/<int:pk>/', views.atualiza_usuarios, name='atualiza_usuarios'),
    path('exclui_usuarios/<int:pk>/', views.exclui_usuarios, name='exclui_usuarios'),
    path('apiuser/<str:loginuser>/', views.apiuser, name='apiuser'),
    path('apiplanofinanceiro/<str:departamento>/', views.apiplanofinanceiro, name='apiplanofinanceiro'),
]