from catalogos.models import Vehiculo, Propietario, Oficina
from django.shortcuts import render

def home(request):
    # Obtener conteos para mostrar en home
    total_vehiculos = Vehiculo.objects.count()
    total_propietarios = Propietario.objects.count()
    total_oficinas = Oficina.objects.filter(activo=True).count()
    
    return render(request, 'home.html', {
        'total_vehiculos': total_vehiculos,
        'total_propietarios': total_propietarios,
        'total_oficinas': total_oficinas,
        'total_activos': '100%',  # Puedes cambiar esto si tienes lógica de status
    })
    