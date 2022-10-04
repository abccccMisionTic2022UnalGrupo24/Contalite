from django import forms
from Transacciones.models import Transaccion


class TransaccionForm(forms.ModelForm):
   
    class Meta: 
        model= Transaccion
        fields=[
            'tipo',
            'usuario',
            'concepto',
            'monto', 
            'id_emp',  
        ]
        labels ={
            'tipo':'Tipo de Transaccion',
            'usuario':'Usuario que realiza',
            'concepto':'Concepto',
            'monto':"Monto",
            'id_emp':"Empresas"
        }
    Widgets ={
            'tipo': forms.Select(attrs={"class":"form"}), 
            'usuario': forms.Select(attrs={"class":"form"}),
            'id_emp': forms.Select(attrs={"class":"form"}), 
            'concepto': forms.TextInput(attrs={'class':'form-control'}),   
            'monto': forms.TextInput(attrs={'class':'form-control'}),
            
        }
