from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login  # Alias para evitar conflicto
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth import logout

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Usar alias para la función login
            if user.userprofile.user_type == 'admin':
                return redirect('administrador')  # Redirige al dashboard del administrador
            elif user.userprofile.user_type == 'docente':
                return redirect('docente')  # Redirige al dashboard del docente
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, intenta de nuevo.')
    return render(request, 'login.html')

def logout_view(request): 
    logout(request) 
    messages.success(request, 'Has cerrado sesión exitosamente.') 
    return redirect('login') # Redirige a la página de login después del cierre de sesión