from django import forms
from django.contrib.auth import get_user_model
from betterforms.multiform import MultiModelForm
from core.models import Usuario,Comuna,Funcionario
from django.contrib.auth.forms import UserCreationForm

User = get_user_model

class defaultForm(UserCreationForm):
    model = User
    fields = ['username','password1','password2']
    
class usForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ['nombre','apellido','rut','telefono','direccion','comuna']


class UsuarioForm(MultiModelForm):

    form_classes = {
        'user': defaultForm,
        'usuario': usForm, 
    }

    
class funForm(forms.ModelForm):
    
    class Meta:
        model = Funcionario
        fields = ['nombre','apellido','rut']


class FuncionarioForm(MultiModelForm):

    form_classes = {
        'user': defaultForm,
        'funcionario': funForm, 
    }
