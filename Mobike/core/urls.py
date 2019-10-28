from django.urls import path
from .views import IndexPageView

urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
    #path('login/', LoginPageView.as_view(), name='login'),
    #path('registro/', RegistroPageView.as_view(), name='registro'),
]

