#from Empresas.views import empresaListView
from django.urls import path
from Empresas import views



urlpatterns = [
        path('registeremp/', views.regEmp, name='register'),
        path('listar/', views.listemp, name='listarEmp'),
        path('listarbyid/<str:emp_id>', views.listempbyid, name='listarEmpbyid'),
        path('editaremp/<str:emp_id>', views.updateemp, name='updateEmpresa'),
        path('eliminaremp/<str:emp_id>', views.deleteEmp, name='deleteEmpesas'),
        path('consultaremp/',views.consultemp, name='buscar Empresas'),
        
    ]
