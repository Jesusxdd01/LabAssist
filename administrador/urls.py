from django.urls import path
from .views import administrador

urlpatterns = [
    path('', administrador, name='administrador'),
]
