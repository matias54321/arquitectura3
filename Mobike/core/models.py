from django.db import models

# Create your models here.
class Funcionario(models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellido = models.CharField(max_length=100, blank=False, null=False)
    rut = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
        ordering = ['rut']

    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Comuna(models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    

class Usuario(models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellido = models.CharField(max_length=100, blank=False, null=False)
    rut = models.CharField(max_length=100, blank=False, null=False)
    telefono = models.CharField(max_length=100, blank=False, null=False)
    direccion = models.CharField(max_length=100, blank=False, null=False)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    aprobado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['rut']

    def __str__(self):
        return self.nombre + ' ' + self.apellido
    
    
class Aprobacion(models.Model):
    id= models.AutoField(primary_key=True)
    funcionario=models.ForeignKey(Funcionario,on_delete=models.CASCADE)
    usuario=models.ForeignKey(Usuario ,on_delete=models.CASCADE)
    estado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Aprobacion'
        verbose_name_plural = 'Aprobaciones'
        ordering = ['estado']

    def __str__(self):
        return 'Aprobación' + str(self.id)