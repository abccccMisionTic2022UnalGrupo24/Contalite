from django.db import models
from .user import User

class Transaccion(models.Model):
    id_tr=models.BigAutoField(unique=True,primary_key=True)
    tipo=models.CharField("Ingreso - Egreso",max_length=50,null=False)
    fecha_tr=models.DateField(auto_now=True)
    usuario=models.ForeignKey(User,related_name="transaccion", on_delete=models.CASCADE)
    concepto=models.TextField("Concepto",max_length=500,null=False) 
    monto=models.IntegerField("Monto",max_length=20,null=False)