from django.db import models

class Empresa(models.Model):
    nit=models.BigAutoField(unique=True,primary_key=True)
    direccion=models.CharField("Direccion",null=False,max_length=100)
    fecha_creacion_emp=models.DateField(auto_now=True)
    nom_emp=models.CharField("Nombre Empresa",null=False, max_length=25)
    sec_prod=models.CharField("Senctor Productivo",null=False, max_length=25)
    ciudad=models.CharField("Ciudad",null=False,max_length=100)
    telefono=models.CharField("Telefono",null=False,max_length=100)