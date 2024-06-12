from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from .forms import UsuarioForm, ParqueForm, ZonaForm, BrigadaForm
from .models import Usuario


def panel_crear(request):
    usuarios = {'usuarios': Usuario.objects.all()}
    return render(request, 'panel_crear.html', usuarios)

# Vista para crear un nueva zona
def crear_zona(request):
    if request.method == 'POST':
        form = ZonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('in_datos')
    else:
        form = ZonaForm()
    return render(request, 'crear_zona.html', {'form': form})
# Vista para crear un nuevo parque
def crear_parque(request):
    if request.method == 'POST':
        form = ParqueForm(request.POST)
        if form .is_valid():
            form .save()
            return redirect('in_datos') 
    else:
        form  = ParqueForm()
    return render(request, 'crear_parque.html', {'form': form })
# Vista para crear un nueva brigada
def crear_brigada(request):
    if request.method == 'POST':
        form = BrigadaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('in_datos')
    else:
        form = BrigadaForm()
    return render(request, 'crear_brigada.html', {'form': form})
# Vista para crear un nuevo usuario
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UsuarioForm()
    return render(request, 'crear_user.html', {'form': form})

# Vista para editar un usuario existente
def editar_usuario(request, id):
    # usuario = get_object_or_404(Usuario, numero_casco=numero_casco)
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('editar_usuario', id=id)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'editar_usuario.html', {'form': form})

# Vista para eliminar un usuario existente
def eliminar_usuario(request,id):
    # usuario = get_object_or_404(Usuario, numero_casco=numero_casco)
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'eliminar_usuario.html', id=id)






