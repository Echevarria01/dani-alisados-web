from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from productos.models import Producto
from productos.forms import ProductoForm

def solo_staff(user):
    return user.is_staff


@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

    
@login_required
def dashboard_home(request):
    if not request.user.is_staff:
        return redirect('dashboard:productos')

    return render(request, 'dashboard/home.html')


@login_required
def productos_list(request):
    if not request.user.is_staff:
        return redirect('dashboard:productos')

    productos = Producto.objects.all()
    return render(request, 'dashboard/productos_list.html', {
        'productos': productos
    })


@login_required
def producto_nuevo(request):
    if not request.user.is_staff:
        return redirect('dashboard:productos')

    form = ProductoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard:productos')

    return render(request, 'dashboard/producto_form.html', {
        'form': form,
        'accion': 'Nuevo'
    })


@login_required
def producto_editar(request, pk):
    if not request.user.is_staff:
        return redirect('dashboard:productos')

    producto = get_object_or_404(Producto, pk=pk)
    form = ProductoForm(request.POST or None, request.FILES or None, instance=producto)

    if form.is_valid():
        form.save()
        return redirect('dashboard:productos')

    return render(request, 'dashboard/producto_form.html', {
        'form': form,
        'accion': 'Editar'
    })


@login_required
def producto_eliminar(request, pk):
    if not request.user.is_staff:
        return redirect('dashboard:productos')

    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('dashboard:productos')


# Create your views here.
