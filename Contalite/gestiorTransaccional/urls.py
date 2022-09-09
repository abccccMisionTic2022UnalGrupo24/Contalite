from django.contrib import admin
from django.urls import path
from gestiorTransaccional.views.empleado import EmpleadoView
from gestiorTransaccional.views.empresa import EmpresaView

urlpatterns = [
    #Rutas empleados
    path('empleado/', EmpleadoView.as_view(),name='listar'),
    path('empleado/bus/<str:id_empleado>', EmpleadoView.as_view(),name='buscar'),
    path('empleado/mod/<str:id_empleado>', EmpleadoView.as_view(),name='modificar'),
    path('empleado/del/<str:id_empleado>', EmpleadoView.as_view(),name='borrar'),
    #Rutas  empresas
    path('empresa/', EmpresaView.as_view(),name='listar'),
    path('empresa/bus/<str:nit>', EmpresaView.as_view(),name='buscar'),
    path('empresa/mod/<str:nit>', EmpresaView.as_view(),name='modificar'),
    path('empresa/del/<str:nit>', EmpresaView.as_view(),name='borrar'),
]

