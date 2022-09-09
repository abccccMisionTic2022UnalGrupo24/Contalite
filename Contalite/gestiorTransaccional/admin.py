from django.contrib import admin

<<<<<<< Updated upstream
=======
# Register your models here.
>>>>>>> Stashed changes
from gestiorTransaccional.models.empleado import Empleado
from gestiorTransaccional.models.empresa import Empresa
from gestiorTransaccional.models.transaccion import Transaccion
from gestiorTransaccional.models.user import User

admin.site.register(Empleado)
admin.site.register(Empresa)
admin.site.register(Transaccion)
<<<<<<< Updated upstream
admin.site.register(User)
=======
admin.site.register(User)

# Register your models here.
>>>>>>> Stashed changes
