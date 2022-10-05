from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm, RegistrationForm1
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

def register(request):
    if request.method =='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado con exito')
            return redirect ('/')
    else:
        form=RegistrationForm()
    context={ 'form':form}
    return render(request, 'registrar.html', context)

def register1(request):
    if request.method =='POST':
        form=RegistrationForm1(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado con exito')
            return redirect ('../listar/')
    else:
        form=RegistrationForm1()
    context={ 'form':form}
    return render(request, 'registrar1.html', context)

@login_required
def listarUsu(request):
    users=User.objects.all()
    data={
            'users': users
        }
    print(users)
    return render(request, "listar.html", data)

@login_required
def updateusu(request, id):
    users = User.objects.get(id=id)
    if request.method == 'GET':
        form=RegistrationForm1(instance=users)
    else:
        form=RegistrationForm1(request.POST, instance=users)
        if form.is_valid():
            form.save()
        return redirect("/usuarios/listar")
    return render(request, 'registrar1.html', {'form':form}) 

@login_required
def deleteUser(request, id):
    users = User.objects.get(id=id)
    users.delete()
    return redirect ('/usuarios/listar')

@login_required
def listusubyid(request, id):
    users = User.objects.filter(id=id)
    contexto = {'users': users}
    return render(request, "listarUsuid.html",contexto)

@login_required
def consultemp(request):
    id=request.POST['Id']
    url='/usuarios/listarbyid/'+id
    return redirect(url)

@login_required
def adminview(request):
   return render(request, "ingresoSesionAdmin-Contalite.html")

def logout_request(request):
    logout(request)
    messages.info(request,"Saliste Exitosamente")
    return redirect ('/accounts/login/')

 
