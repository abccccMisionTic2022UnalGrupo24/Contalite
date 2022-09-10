from django.db import models
from .empresa import Empresa
from .user import User

class Empleado (models.Model):
    id_empleado=models.AutoField(auto_created=True,unique=True,primary_key=True)
    id_user=models.OneToOneField(User, on_delete=models.CASCADE)
    nom_emp=models.CharField("Nombres",null=False, max_length=25)
    ape_emp=models.CharField("Apellidos",null=False,max_length=25)
    email=models.EmailField("E-mail",unique=True,null=False,max_length=100)
    telefono=models.CharField("Telefono",null=False,max_length=10)
    empresa=models.ForeignKey(Empresa, related_name='Empresa', on_delete=models.CASCADE)
    fecha_creacion=models.DateField(auto_now=True)
    
