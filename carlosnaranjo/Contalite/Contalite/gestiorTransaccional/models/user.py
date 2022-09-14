from distutils.command.upload import upload
from pyexpat import model
from django.db import models

class User(models.Model): # especificacion para que el framework lo identifique
    id_user=models.BigAutoField(max_length=50,unique=True,primary_key=True)
    nom_usu=models.CharField("Nombre Usuario",unique=True, max_length=20, null=False)
    password=models.CharField("Password",max_length=50, null=False)
    email=models.EmailField("E-mail",unique=True,null=False, max_length=100)
    image = models.ImageField(null=True, blank=True)
    rol=models.CharField("Rol",max_length=20, null=False)