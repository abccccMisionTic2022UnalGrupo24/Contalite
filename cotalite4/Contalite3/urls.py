
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('/', LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('usuarios/', include('Usuarios.urls')),
    path('empresas/', include('Empresas.urls')),
    # path('logout/', LogoutView.as_view(template_name='registration/login.html'), name="logout"),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/',include('Usuarios.urls')),
    path('transacciones/',include('Transacciones.urls')),
    path('accounts/login/',LoginView.as_view(template_name='registration/login.html'), name="login"),
    ]
