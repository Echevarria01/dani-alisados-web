from django.shortcuts import render
from .models import Producto

def home(request):
    return render(request, 'productos/home.html')

def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'productos/catalogo.html', {
        'productos': productos
    })


# Create your views here.
