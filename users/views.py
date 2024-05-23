from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model



# Create your views here.


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
           
            return render(request, 'cadastros/cadastrostipo.html')
        else:
            # messages.warning(request, 'Alguma coisa está incorreta, favor verifique o preenchimento do formulário de login')
            return redirect('login')
    else:
        return render(request, 'users/login.html')
    
def logout_user(request):
    logout(request)
    #messages.info(request, 'Logout com sucesso.')
    return redirect('login')
