from django.shortcuts import render
from django.shortcuts import redirect
from Transacciones.models import Transaccion
from .forms import TransaccionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

def registerTr(request):
    if request.method =='POST':
        form=TransaccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/transacciones/listar/')
    else:
        form=TransaccionForm()
    context={ 'form':form}
    return render(request, 'crearTransaccion-Contalite.html', context)

@login_required
def listartr(request):
    tr=Transaccion.objects.all()
    data={
            'trans': tr
        }
    print(tr)
    return render(request, "visualizarTransaccionContalite.html", data)

@login_required
def updatetr(request, id_tr):
    Trans = Transaccion.objects.get(id_tr=id_tr)
    if request.method == 'GET':
        form=TransaccionForm(instance=Trans)
    else:
        form=TransaccionForm(request.POST, instance=Trans)
        if form.is_valid():
            form.save()
        return redirect("/transacciones/listar")
    return render(request, 'crearTransaccion-Contalite.html', {'form':form}) 

@login_required
def deletetr(request, id_tr):
    tr = Transaccion.objects.get(id_tr=id_tr)
    tr.delete() 
    return redirect ('/transacciones/listar')

@login_required
def listtrbyid(request, id_tr):
    tr = Transaccion.objects.filter(id_tr=id_tr)
    contexto = {'trans': tr}
    return render(request, "listarTrid.html",contexto)

@login_required
def consulttr(request):
    id=request.POST['Id']
    url='/transacciones/listarbyid/'+id
    return redirect(url)
