from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def administrador(request):
    return render(request, 'dashboard.html')  # Asegúrate de tener el template dashboard.html
