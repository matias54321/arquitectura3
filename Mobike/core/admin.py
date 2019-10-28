from django.contrib import admin
from .models import Funcionario
from .models import Comuna
from .models import Usuario
from .models import Aprobacion
# Register your models here.

admin.site.register(Funcionario)
admin.site.register(Comuna)
admin.site.register(Usuario)
admin.site.register(Aprobacion)