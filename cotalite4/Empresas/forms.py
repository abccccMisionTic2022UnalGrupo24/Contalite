from django import forms
from Empresas.models import Empresa

class registraremp(forms.ModelForm):
    
    class Meta: 
        model= Empresa
        fields=[
            'usu_id',
            'nit',
            'direccion',
            'nom_emp',
            'sec_prod',   
            'ciudad',
            'telefono',
        ]
        labels ={
            'usu_id':'Id Usuario que registra',
            'nit':'NIT',
            'direccion':'Direccion',
            'nom_emp':'Nombre de la Empresa',
            'sec_prod':'Sector Productivo',   
            'ciudad':'Ciudad',
            'telefono':'Telefono',
        }
        Widgets ={
            'usu_id': forms.Select(attrs={"class":"form"}),
            'nit': forms.TextInput(attrs={"class":"form"}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'nom_emp': forms.TextInput(attrs={'class':'form-control'}),
            'sec_prod': forms.TextInput(attrs={'class':'form-control'}),   
            'ciudad': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
        }
