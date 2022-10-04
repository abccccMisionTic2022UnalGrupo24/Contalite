from django.contrib import admin
from . import views
#from Usuarios.views import userListView
from django.urls import path


urlpatterns = [
        path('register/', views.registerTr, name='registerTr'),
        path('listar/', views.listartr, name='listartr'),
        path('editar/<str:id_tr>', views.updatetr, name='updatetr'),
        path('eliminar/<str:id_tr>', views.deletetr, name='deletetr'),
        path('consultartr/',views.consulttr, name='buscarrt'),
        path('listarbyid/<str:id_tr>/',views.listtrbyid, name='buscar id'),
        #path('logout/', views.logout_request, name='logout'),
        #path('', views.adminview, name='vista page admin'),        
    ]
    