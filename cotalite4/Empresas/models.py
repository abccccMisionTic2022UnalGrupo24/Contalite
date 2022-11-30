from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    emp_id=models.AutoField(auto_created=True,unique=True,primary_key=True, blank=True)
    usu_id=models.ForeignKey(User,related_name="Usuario", on_delete=models.CASCADE)
    nit=models.CharField("NIT",max_length=150, unique=True)
    direccion=models.CharField("Direccion",null=False,max_length=100)
    fecha_creacion_emp=models.DateField(auto_now=True)
    nom_emp=models.CharField("Nombre Empresa",null=False, max_length=25)
    sec_prod=models.CharField("Senctor Productivo",null=False, max_length=25)
    ciudad=models.CharField("Ciudad",null=False,max_length=100)
    telefono=models.CharField("Telefono",null=False,max_length=100)

    def __str__(self):
            return self.nom_emp