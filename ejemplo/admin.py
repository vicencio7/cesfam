from django.contrib import admin
from ejemplo.models import *
# Register your models here.

admin.site.register(Paciente)
admin.site.register(Contacto)
admin.site.register(Programa)
admin.site.register(Cita)
admin.site.register(Reporte)