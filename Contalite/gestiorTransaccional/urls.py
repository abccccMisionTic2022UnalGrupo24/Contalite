from django.contrib import admin
from django.urls import path
from gestiorTransaccional.views.empleado import EmpleadoView
from gestiorTransaccional.views.empresa import EmpresaView
from gestiorTransaccional.views.transaccion import TransaccionView
from gestiorTransaccional.views.user import UserView

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
    #Rutas  transacciones
    path('transaccion/', TransaccionView.as_view(),name='listar'),
    path('transaccion/bus/<str:nit>', TransaccionView.as_view(),name='buscar'),
    path('transaccion/mod/<str:nit>', TransaccionView.as_view(),name='modificar'),
    path('transaccion/del/<str:nit>', TransaccionView.as_view(),name='borrar'),
    #Rutas  users
    path('user/', UserView.as_view(),name='listar'),
    path('user/bus/<str:nit>', UserView.as_view(),name='buscar'),
    path('user/mod/<str:nit>', UserView.as_view(),name='modificar'),
    path('user/del/<str:nit>', UserView.as_view(),name='borrar'),
]