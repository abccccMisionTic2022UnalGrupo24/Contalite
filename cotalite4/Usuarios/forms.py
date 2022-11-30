import email
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
   
    class Meta: 
        model= User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
            
        ]
        labels ={
            'username':'Nombre de usuario',
            'first_name':'Nombre',
            'last_name':'Apellido',
            'email':'E-mail',
            
            
        }

class RegistrationForm1(UserCreationForm):
   
    class Meta: 
        model= User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
            'is_superuser',   
            'is_staff',
        ]
        labels ={
            'username':'Nombre de usuario',
            'first_name':'Nombre',
            'last_name':'Apellido',
            'email':'E-mail',
            'is_superuser':"Rol",
            'is_staff':'staff',
        }
    
