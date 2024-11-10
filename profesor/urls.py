from django.urls import path
from .views import docente

urlpatterns = [
    path('', docente, name='docente'),
]
