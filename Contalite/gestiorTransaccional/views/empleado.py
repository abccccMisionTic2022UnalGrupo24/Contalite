from django.shortcuts import render

import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from gestiorTransaccional.models import Empleado
from django.http import JsonResponse


class EmpleadoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,  id_empleado='' ):
        
        if len(id_empleado)>0:
            emp = list(Empleado.objects.filter(id_empleado=id_empleado).values())
            if len(emp)>0:
                datos={"mensaje": emp}
            else:
                datos={'mensaje':'no se encontraron empleados'}
            return JsonResponse(datos)
        else:
            emp=list(Empleado.objects.values())
            if len(emp)>0:
                datos={"mensaje": emp}
            else:
                datos={'mensaje':'no se encontraron empleados'}
            return JsonResponse(datos) 

    def post(self, request):# agregar
        data=json.loads(request.body)
        crear_emp = Empleado(id_user_id=data['id_user_id'],nom_emp=data['nom_emp'],ape_emp=data['ape_emp'],email=data['email'],telefono=data['telefono'],empresa_id=data['empresa_id'],fecha_creacion=data['fecha_creacion'])
        crear_emp.save()
        datos={'mensaje':'empleado registrado exitosamente'}
        return JsonResponse(datos)   

    def put(self, request, id_empleado): # modificar
        data = json.loads(request.body)
        emp= list(Empleado.objects.filter(id_empleado=id_empleado).values())
        if len(emp)>0:
            m_empleado=Empleado.objects.get(id_empleado=id_empleado)
            #m_empleado.id_empleado=data["id_empleado"]
            #m_empleado.id_user=data["id_user"]
            m_empleado.nom_emp=data["nom_emp"]
            m_empleado.ape_emp=data["ape_emp"]
            m_empleado.email=data["email"]
            m_empleado.telefono=data["telefono"]
            m_empleado.empresa_id=data["empresa_id"]
            m_empleado.fecha_creacion=data["fecha_creacion"]
            m_empleado.save()
            mensaje={"mensaje":"empleado actualizado exitosamente"}
        else:
            mensaje={"mensaje":"No se encontro el empleado."} 

        return JsonResponse(mensaje)    

    def delete(self,request,id_empleado):
        emp=list(Empleado.objects.filter(id_empleado=id_empleado).values())
        if len(emp)>0:
            Empleado.objects.filter(id_empleado=id_empleado).delete()
            mensaje={"mensaje":"Empleado eliminado exitosamente."}
        else:
            mensaje={"mensaje":"No se encontro el empleado."}

        return JsonResponse(mensaje)