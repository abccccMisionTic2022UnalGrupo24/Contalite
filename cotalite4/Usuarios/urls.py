from django.contrib import admin
from . import views
#from Usuarios.views import userListView
from django.urls import path


urlpatterns = [
        path('register/', views.register, name='register'),
        path('register1/', views.register1, name='register1'),
        path('listar/', views.listarUsu, name='empleados'),
        path('editar/<str:id>', views.updateusu, name='updateusu'),
        path('eliminar/<str:id>', views.deleteUser, name='deleteUser'),
        path('consultar/',views.consultemp, name='buscar usuarios'),
        path('listarbyid/<str:id>/',views.listusubyid, name='buscar id'),
        path('logout/', views.logout_request, name='logout'),
        path('', views.adminview, name='vista page admin'), 
    ]
    