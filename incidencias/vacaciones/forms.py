from django import forms
from .models import Usuario, Parque, Zona, Brigada, Vacaciones
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User



class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        
class ParqueForm(forms.ModelForm):
    class Meta:
        model = Parque
        fields = '__all__'
        
class ZonaForm(forms.ModelForm):
    class Meta:
        model = Zona
        fields = '__all__'
        
class BrigadaForm(forms.ModelForm):
    class Meta:
        model = Brigada
        fields = '__all__'
        
class VacacionesForm(forms.ModelForm):
    class Meta:
        model = Vacaciones
        fields ='__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
            'dias_totales': forms.HiddenInput(),
        }  

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }

       
class LoginForm(AuthenticationForm):
   class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }