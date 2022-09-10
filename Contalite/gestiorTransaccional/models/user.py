from distutils.command.upload import upload
from django.db import models

class User(models.Model): # especificacion para que el framework lo identifique
    id_user=models.AutoField(auto_created=True,unique=True,primary_key=True)
    nom_usu=models.CharField("Nombre Usuario",unique=True, max_length=20, null=False)
    password=models.CharField("Password",max_length=50, null=False)
    email=models.EmailField("E-mail",unique=True,null=False, max_length=100)
    image = models.ImageField(null=True, blank=True)
    admin=models.BooleanField("Rol", null=True)
   
    def __str__(self):
        return "%s id_user:" % self.id_user