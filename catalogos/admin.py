from django.contrib import admin

from .models import Vehiculo, Propietario, Oficina, Placa

# Register your models here.

admin.site.register(Vehiculo)
admin.site.register(Propietario)
admin.site.register(Oficina)
admin.site.register(Placa)