from django.shortcuts import render
from Empresas.forms import registraremp
from Empresas.models import Empresa
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def home(request):
    return redirect ('http://127.0.0.1:8000')

@login_required
def regEmp(request):
    if request.method == 'POST':
        form = registraremp(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('http://127.0.0.1:8000/empresas/listar/')
    else:
        form=registraremp()
        context={'form':form}
        return render(request, 'crearEmpresa-contalite.html', context)

@login_required
def listemp(request):
    empresas = Empresa.objects.all()
    contexto = {'empresas':empresas}
    return render(request, "listarEmp.html",contexto)

@login_required
def listempbyid(request, emp_id):
    empresas = Empresa.objects.filter(emp_id=emp_id)
    contexto = {'empresas':empresas}
    return render(request, "listarEmpid.html",contexto)

@login_required
def consultemp(request):
    id=request.POST['Id']
    url='http://127.0.0.1:8000/empresas/listarbyid/'+id
    return redirect(url)

@login_required
def updateemp(request, emp_id):
    emp = Empresa.objects.get(emp_id=emp_id)
    if request.method == 'GET':
        form=registraremp(instance=emp)
    else:
        form=registraremp(request.POST, instance=emp)
        if form.is_valid():
            form.save()
        return redirect("http://127.0.0.1:8000/empresas/listar")
    return render(request, 'crearEmpresa-contalite.html', {'form':form}) 

@login_required
def deleteEmp(request, emp_id):
    Emp = Empresa.objects.get(emp_id=emp_id)
    Emp.delete()
    return redirect ('http://127.0.0.1:8000/empresas/listar')




