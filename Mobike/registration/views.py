from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UsuarioForm,FuncionarioForm
# Create your views here.

class RegistroView(CreateView):
    form_class = UsuarioForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registro.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'
    
class RegistroFunView(CreateView):
    form_class = FuncionarioForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registro_fun.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'
     

