from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def docente(request):
    return render(request, 'dashboardP.html')  # Asegúrate de tener el template dashboardP.html
