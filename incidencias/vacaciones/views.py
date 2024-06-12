from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from .forms import UsuarioForm, ParqueForm, ZonaForm, BrigadaForm
from .models import Usuario
from django.shortcuts import render


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


# Vista para listar todos los usuarios
def listar_usuarios(request):
    usuarios = {'usuarios': Usuario.objects.all()}  # Retrieve all Usuario objects from the database
    return render(request, 'lis_user.html', usuarios)  # Render the 'lis_user.html' template with the usuarios data

def panel_crear(request):
    return render(request, 'panel_crear.html')



# # # Vista para editar un usuario existente
# # def editar_usuario(request, id):
# #     usuario = get_object_or_404(User, id=id)
# #     if request.method == 'POST':
# #         form = UserForm(request.POST, instance=usuario)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('listar_usuarios')
# #     else:
# #         form = UserForm(instance=usuario)
# #     return render(request, 'vacaciones/editar_usuario.html', {'form': form})

# # Vista para eliminar un usuario existente
# def eliminar_usuario(request, id):
#     usuario = get_object_or_404(User, id=id)
#     if request.method == 'POST':
#         usuario.delete()
#         return redirect('listar_usuarios')
#     return render(request, 'vacaciones/eliminar_usuario.html', {'usuario': usuario})