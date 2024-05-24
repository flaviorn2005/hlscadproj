from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from .models import PlanoFinanceiro, Usuario
from .form import PlanofinanceiroForm, UsuarioForm

from django.http import JsonResponse

# Create your views here.

@login_required
def tipo_cadastro(request):



    return render(request, 'cadastros/cadastrostipo.html')

# def cadastro_usuario(request):


#     return render(request, 'cadastros/cadastros.html')

@login_required
def cadastro_planofinanceiro(request):
    if request.method == 'POST':
        form = PlanofinanceiroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro_planofinanceiro')

    else:
        form = PlanofinanceiroForm()
        
        context = {'form':form}
        return render(request, 'cadastros/cadastros.html', context)


    #return render(request, 'cadastros/cadastros.html')

@login_required
def cadastro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro_usuario')
        else:
            return HttpResponse("formularioinvalido")
    else:
        form = UsuarioForm()
        
        context = {'form':form}
        return render(request, 'cadastros/cadastros.html', context)

@login_required
def todos_planosfinaceiros(request):

    planosfinanceiros = PlanoFinanceiro.objects.filter(Ativo=True).order_by('Plano_financeiro')
    context = {'planosfinanceiros':planosfinanceiros}
    return render(request, 'cadastros/todospf.html', context)

@login_required
def todos_usuarios(request):
    usuarios = Usuario.objects.filter(Ativo=True).order_by('Usuario')
    context = {'usuarios':usuarios}
    return render(request, 'cadastros/todosusuarios.html', context)




@login_required
def atualiza_planosfinanceiros(request, pk):
    planofinanceiro = PlanoFinanceiro.objects.get(pk=pk)
    if request.method == 'POST':
        
        form = PlanofinanceiroForm(request.POST, instance=planofinanceiro)
        if form.is_valid():
            form.save()
            return redirect('todos_planosfinanceiros')

    else:
        form = PlanofinanceiroForm(instance=planofinanceiro)
        context = {'form':form}
        return render(request, 'cadastros/cadastros.html', context)

@login_required
def atualiza_usuarios(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    if request.method == 'POST':
        
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('todos_usuarios')

    else:
        form = UsuarioForm(instance=usuario)
        context = {'form':form}
        return render(request, 'cadastros/cadastros.html', context)



@login_required
def exclui_planosfinanceiros(request, pk):
    planofinanceiro = PlanoFinanceiro.objects.get(pk=pk)
    planofinanceiro.Ativo = False
    planofinanceiro.save()
    return redirect('todos_planosfinanceiros')

@login_required
def exclui_usuarios(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    usuario.Ativo = False
    usuario.save()
    return redirect('todos_usuarios')


def apiuser(request, loginuser):
    resultados = Usuario.objects.filter(Ativo=True, Usuario=loginuser)
    #print(request.headers.get('senha'))
    if request.method == 'GET' and request.headers.get('senha') == 'qweasd':
        if resultados:
            print(resultados[0].Departamento)

            resultadosjson = [{
                'departamento': resultados[0].Departamento,
                'senha': resultados[0].Senha_do_usuario,
                
            }]
            
            return JsonResponse(resultadosjson, safe=False)
        else:
            resultadosjson = [{
                'departamento': 'erro',
                'senha': 'erro',
                
            }]
            return JsonResponse(resultadosjson, safe=False)
    else:
        return HttpResponse('Não permitido')

    
def apiplanofinanceiro(request, departamento):
    # resultados = PlanoFinanceiro.objects.all().values('Plano_financeiro', 'Departamento')
    resultados = PlanoFinanceiro.objects.filter(Ativo=True, Departamento=departamento)
    lista_planos = []
    for plano in resultados:
        lista_planos.append(plano.Plano_financeiro)

    #resultados_list = list(resultados)
    #print(request.headers.get('senha'))
    if request.method == 'GET' and request.headers.get('senha') == 'qweasd':
        if resultados:
            return JsonResponse(lista_planos, safe=False)
        else:
            resultadosjson = [{
                'departamento': 'erro',
                'senha': 'erro',
                
            }]
            return JsonResponse(resultadosjson, safe=False)
    else:
        return HttpResponse('Não permitido')

    
