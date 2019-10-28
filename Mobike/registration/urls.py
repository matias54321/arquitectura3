from django.urls import path
from .views import RegistroView,RegistroFunView
from . import views

urlpatterns = [
    path("registro/", RegistroView.as_view(), name="registro"),
    path("registro_fun/", RegistroFunView.as_view(), name="registro_fun"),
    #path("registro/", views.datosUsuario, name="registro")
]
