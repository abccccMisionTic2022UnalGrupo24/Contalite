from django.shortcuts import render
import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from gestiorTransaccional.models import User
from django.http import JsonResponse


class UserView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,  id_user='' ):
        
        if len(id_user)>0:
            user = list(User.objects.filter(id_user=id_user).values())# Estructura = variable = list(clase)
            if len(user)>0:
                datos={"mensaje": user}
            else:
                datos={'mensaje':'no se encontro el Usuario'}
            return JsonResponse(datos)
        else:
            user=list(User.objects.values())
            if len(user)>0:
                datos={"mensaje": user}
            else:
                datos={'mensaje':'no se encontro el usuario'}
            return JsonResponse(datos) 

    def post(self, request):
        data=json.loads(request.body)
        crear_user= User(id_user=data['id_user'],nom_usu=data['nom_usu'],password=data['password'],email=data['email'],image=data['image'],rol=data['rol'])
        crear_user.save()
        datos={'mensaje':'Usuario registrado exitosamente'}
        return JsonResponse(datos)   

    def put(self, request, id_user):
        data = json.loads(request.body)
        user= list(User.objects.filter(id_user=id_user).values())
        if len(user)>0:
            mod_user=User.objects.get(id_user=id_user)
            mod_user.id_user=data["id_user"]
            mod_user.nom_usu=data["nom_usu"]
            mod_user.password=data["password"]
            mod_user.email=data["email"]
            mod_user.image=data["image"]
            mod_user.rol=data["rol"]
            mod_user.save()
            mensaje={"mensaje":"Usuario actualizado exitosamente"}
        else:
            mensaje={"mensaje":"No se encontro el usuario."} 
        return JsonResponse(mensaje)    

    def delete(self,request, id_user):
        user=list(User.objects.filter(id_user=id_user).values())
        if len(user)>0:
            User.objects.filter(id_user=id_user).delete()
            mensaje={"mensaje":"Usuario eliminado exitosamente."}
        else:
            mensaje={"mensaje":"No se encontro el usuario."}
        return JsonResponse(mensaje)