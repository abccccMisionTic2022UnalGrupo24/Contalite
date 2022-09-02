from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Rol(models.Model):
    id_rol=models.IntegerField(max_length=50, primary_key=True)
    administrador=models.BooleanField(unique=True,null=True)
    empleado=models.BooleanField(null=False,unique=True)

class tipo(models.Model):
    id_tr=models.IntegerField(unique=True,primary_key=True,primary_key=True)
    ingreso=models.BooleanField(null=True)
    egreso=models.BooleanField(null=True)
    
class Transaccion(models.Model):
    id_em=models.TextField(unique=True,primary_key=True)
    tipo_Trans=models.ForeignKey(tipo, on_delete=models.CASCADE)
    fecha=models.DateField(auto_now=True)
    concepto=models.TextField(max_length=500,null=False) 
    valor=models.IntegerField(max_length=20,null=False)

class Telefono(models.Model):
    telefono=models.IntegerField(max_length=13,null=False,primary_key=True)
    pbx=models.IntegerField(max_length=13,null=True)
    cel=models.IntegerField(max_length=13,null=True)
    what=models.IntegerField(max_length=13,null=True)
    
class Empresa(models.Model):
    nombre_emp=models.TextField(null=False,unique=True,max_length=100,primary_key=True)
    nit=models.ForeignKey(Transaccion,on_delete=models.CASCADE)
    dir_emp=models.TextField(null=False,max_length=100)
    telefono=models.ForeignKey(Telefono,on_delete=models.CASCADE)
    #odels.DateField(auto_now=True)

class Nombre(models.Model):
    primer_nombre=models.TextField(max_length=50,null=False,primary_key=True)
    segundo_nombre=models.TextField(max_length=50,unique=True,null=True)
  
class Apellido(models.Model):
    primer_apellido=models.TextField(max_length=50,null=False,primary_key=True)
    segundo_apellido=models.TextField(max_length=50,unique=True,null=True)
      
class User(models.Model): # especificacion para que el framework lo identifique
    id_user=models.CharField(max_length=50,unique=True,primary_key=True)
    nit=models.ForeignKey(Empresa,on_delete=models.CASCADE)
    nombre=models.ForeignKey(Nombre,on_delete=models.CASCADE)
    apellido=models.ForeignKey(Apellido,on_delete=models.CASCADE)
    usuario=models.CharField(max_length=50,null=False)
    contrasenia=models.CharField(max_length=50,null=False)
    email=models.EmailField(unique=True)
    rol=models.ForeignKey(Rol,on_delete=models.CASCADE)