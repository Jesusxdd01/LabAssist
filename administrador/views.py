from django.shortcuts import render

def administrador(request):
    return render(request, 'dashboard.html')  # Asegúrate de tener el template dashboard.html
