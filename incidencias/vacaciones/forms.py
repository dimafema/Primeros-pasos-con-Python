from django import forms
from .models import Usuario, Parque, Zona, Brigada



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
        
        