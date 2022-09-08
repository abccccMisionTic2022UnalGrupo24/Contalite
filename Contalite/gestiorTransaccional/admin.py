from django.contrib import admin

from gestiorTransaccional.models.empleado import Empleado
from gestiorTransaccional.models.empresa import Empresa
from gestiorTransaccional.models.transaccion import Transaccion
from gestiorTransaccional.models.user import User

admin.site.register(Empleado)
admin.site.register(Empresa)
admin.site.register(Transaccion)
admin.site.register(User)