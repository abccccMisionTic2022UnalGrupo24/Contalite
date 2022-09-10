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
    path('empleado/cre/', EmpleadoView.as_view(),name='crear'),
    #Rutas  empresas
    path('empresa/', EmpresaView.as_view(),name='listar'),
    path('empresa/bus/<str:nit>', EmpresaView.as_view(),name='buscar'),
    path('empresa/mod/<str:nit>', EmpresaView.as_view(),name='modificar'),
    path('empresa/del/<str:nit>', EmpresaView.as_view(),name='borrar'),
    path('empresa/cre/', EmpresaView.as_view(),name='crear'),
    #Rutas  transacciones
    path('transaccion/', TransaccionView.as_view(),name='listar'),
    path('transaccion/bus/<str:id_tr>', TransaccionView.as_view(),name='buscar'),
    path('transaccion/mod/<str:id_tr>', TransaccionView.as_view(),name='modificar'),
    path('transaccion/del/<str:id_tr>', TransaccionView.as_view(),name='borrar'),
    path('transaccion/cre/', TransaccionView.as_view(),name='crear'),
    #Rutas  users
    path('user/', UserView.as_view(),name='listar'),
    path('user/bus/<str:id_user>', UserView.as_view(),name='buscar'),
    path('user/mod/<str:id_user>', UserView.as_view(),name='modificar'),
    path('user/del/<str:id_user>', UserView.as_view(),name='borrar'),
    path('user/cre/', UserView.as_view(),name='crear'),
]