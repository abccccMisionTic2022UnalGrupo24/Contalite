
from django.shortcuts import render
import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from gestiorTransaccional.models import Transaccion
from django.http import JsonResponse


class TransaccionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,  id_tr='' ):
        
        if len(id_tr)>0:
            trans = list(Transaccion.objects.filter(id_tr=id_tr).values())# Estructura = variable = list(clase)
            if len(trans)>0:
                datos={"mensaje": trans}
            else:
                datos={'mensaje':'no se encontraron transacciones'}
            return JsonResponse(datos)
        else:
            trans=list(Transaccion.objects.values())
            if len(trans)>0:
                datos={"mensaje": trans}
            else:
                datos={'mensaje':'no se encontro la transaccion'}
            return JsonResponse(datos) 

    def post(self, request):
        data=json.loads(request.body)
        crear_tr = Transaccion(id_tr=data['id_tr'],tipo=data['tipo'],fecha_tr=data['fecha_tr'],usuario_id=data['usuario_id'],concepto=data['concepto'],monto=data['monto'])
        crear_tr.save()
        datos={'mensaje':'Transaccion registrada exitosamente'}
        return JsonResponse(datos)   

    def put(self, request, id_tr):
        data = json.loads(request.body)
        tr= list(Transaccion.objects.filter(id_tr=id_tr).values())
        if len(tr)>0:
            mod_trans=Transaccion.objects.get(id_tr=id_tr)
            mod_trans.id_tr=data["id_tr"]
            mod_trans.tipo=data["tipo"]
            mod_trans.fecha_tr=data["fecha_tr"]
            mod_trans.usuario_id=data["usuario_id"]
            mod_trans.concepto=data["concepto"]
            mod_trans.monto=data["monto"]
            mod_trans.save()
            mensaje={"mensaje":"Transaccion actualizada exitosamente"}
        else:
            mensaje={"mensaje":"No se encontro la transaccion."} 
        return JsonResponse(mensaje)    

    def delete(self,request, id_tr):
        tra=list(Transaccion.objects.filter(id_tr=id_tr).values())
        if len(tra)>0:
            Transaccion.objects.filter(id_tr=id_tr).delete()
            mensaje={"mensaje":"Transaccion eliminada exitosamente."}
        else:
            mensaje={"mensaje":"No se encontro la transaccion."}

        return JsonResponse(mensaje)