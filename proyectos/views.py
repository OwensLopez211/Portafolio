from django.shortcuts import render
from .models import proyectos

# Create your views here.

def home(request):
    proyecto = proyectos.objects.all()
    return render(request, 'home.html', {'Proyectos': proyecto})