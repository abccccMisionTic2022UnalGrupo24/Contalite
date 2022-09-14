from django.db import models
from .empresa import Empresa

class Empleado (models.Model):
    id_empleado=models.BigAutoField(null=False,unique=True,primary_key=True)
    nom_emp=models.CharField("Nombres",null=False, max_length=25)
    ape_emp=models.CharField("Apellidos",null=False,max_length=25)
    email=models.EmailField("E-mail",unique=True,null=False,max_length=100)
    telefono=models.CharField("Telefono",null=False,max_length=10)
    empresa=models.ForeignKey(Empresa, related_name='Empresa', on_delete=models.CASCADE)
    
    fecha_creacion=models.DateField(auto_now=True)