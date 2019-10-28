from django.views.generic.base import TemplateView
#from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.utils import timezone
#from django import forms
from .models import Usuario
from .models import Funcionario
from .models import Aprobacion  

# Create your views here.

#class RegistroPageView(CreateView):
    #form_class = UserCreationForm
    #template_name = 'core/registro.html'

    #def get_success_url(self):
        #return reverse_lazy('login') + '?register'   
        #return render(request, 'core/login.html', {})

class IndexPageView(TemplateView):
    template_name = "core/index.html"
      
    def get(self,request,*args, **kwargs):
        return render(request, self.template_name, {'title':"Let's Mobike !"})

#class LoginPageView(TemplateView):
    #template_name = "core/login.html"
    #return render(request, 'core/login.html', {})

