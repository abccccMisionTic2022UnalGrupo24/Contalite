from django.shortcuts import render
import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from gestiorTransaccional.models import Empresa
from django.http import JsonResponse


class EmpresaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,  nit='' ):
        
        if len(nit)>0:
            empre = list(Empresa.objects.filter(nit=nit).values())# Estructura = variable = list(clase)
            if len(empre)>0:
                datos={"mensaje": empre}
            else:
                datos={'mensaje':'no se encontro la empresa'}
            return JsonResponse(datos)
        else:
            empre=list(Empresa.objects.values())
            if len(empre)>0:
                datos={"mensaje": empre}
            else:
                datos={'mensaje':'no se encontro la empresa'}
            return JsonResponse(datos) 

    def post(self, request):
        data=json.loads(request.body)
        crear_empre = Empresa(direccion=data['direccion'],fecha_creacion_emp=data['fecha_creacion_emp'],nom_emp=data['nom_emp'],sec_prod=data['sec_prod'],ciudad=data['ciudad'],telefono=data['telefono'])
        crear_empre.save()
        datos={'mensaje':'Empresa registrada exitosamente'}
        return JsonResponse(datos)   

    def put(self, request, nit):
        data = json.loads(request.body)
        empre= list(Empresa.objects.filter(nit=nit).values())
        if len(empre)>0:
            mod_empresa=Empresa.objects.get(nit=nit)
            #mod_empresa.nit=data["nit"]
            mod_empresa.direccion=data["direccion"]
            mod_empresa.fecha_creacion_emp=data["fecha_creacion_emp"]
            mod_empresa.nom_emp=data["nom_emp"]
            mod_empresa.sec_prod=data["sec_prod"]
            mod_empresa.ciudad=data["ciudad"]
            mod_empresa.telefono=data["telefono"]
            mod_empresa.save()
            mensaje={"mensaje":"Empresa actualizada exitosamente"}
        else:
            mensaje={"mensaje":"No se encontro la empresa."} 

        return JsonResponse(mensaje)    

    def delete(self,request, nit):
        empre=list(Empresa.objects.filter(nit=nit).values())
        if len(empre)>0:
            Empresa.objects.filter(nit=nit).delete()
            mensaje={"mensaje":"Empresa eliminada exitosamente."}
        else:
            mensaje={"mensaje":"No se encontro la empresa."}

        return JsonResponse(mensaje)