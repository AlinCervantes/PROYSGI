from django.shortcuts import render, HttpResponse, redirect
from .models import Oficina, Vehiculo, Propietario
from .forms import OficinaForm, VehiculoForm, PropietarioForm
from django.db.models import Q # Importar Q para consultas complejas
from django.db.models import Count

# Create your views here.
def homeCatalogos(request):
    return render(
        request,
        'homeCatalogos.html'
    )
    
def oficinaListar(request):
    oficinas = Oficina.objects.all()
    
    ciudad = request.GET.get('ciudad', '')
    if ciudad:
        oficinas = oficinas.filter(ciudad=ciudad)
    
    activa = request.GET.get('activa', '')
    if activa == 'true':
        oficinas = oficinas.filter(activa=True)
    elif activa == 'false':
        oficinas = oficinas.filter(activa=False)
    
    ciudades = Oficina.objects.values_list('ciudad', flat=True).distinct()
    
    return render(request, 'oficinas_listar.html', {
        'oficinas': oficinas,
        'ciudades': ciudades
    })

def oficinasCrear(request):
    if request.method == 'POST':
        form = OficinaForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('oficinasListar')
    else:
        form = OficinaForm()
    return render (request, 'oficinas_crear.html', {'form':form})

def oficinasEditar(request, id):
    oficina = Oficina.objects.get(id=id)
    if request.method == 'GET':
        form = OficinaForm(instance = oficina)     # Pinta formulario con datos existentes
    else:
        form = OficinaForm(request.POST, instance=oficina) # Se ha hecho alguna modificacion
        if form.is_valid():
            form.save()                                    # Lo guarda 
        return redirect ('oficinasListar')
    
    return render (request, 'oficinas_crear.html', {'form':form})

def oficinasEliminar(request, pk):
    oficina = Oficina.objects.get(pk=pk)
    if request.method == 'POST':            # Se confirma eliminar
        oficina.delete()                    # Se borra registro de la BD
        return redirect('oficinasListar')   # Se redirecciona al listado
    return render (request, 'oficinas_eliminar.html', {'oficina':oficina}) 
                          
def vehiculosListar(request):
    vehiculos = Vehiculo.objects.all()
    
    # FILTRO por búsqueda
    search = request.GET.get('search', '')
    if search:
        vehiculos = vehiculos.filter(
            Q(NIV__icontains=search) |
            Q(marca__icontains=search) |
            Q(linea__icontains=search) |
            Q(modelo__icontains=search) |
            Q(color__icontains=search)
        )
    
    # FILTRO por marca
    marca = request.GET.get('marca', '')
    if marca:
        vehiculos = vehiculos.filter(marca__iexact=marca)
    
    # FILTRO por color
    color = request.GET.get('color', '')
    if color:
        vehiculos = vehiculos.filter(color__iexact=color)
    
    # Obtener opciones únicas para filtros
    marcas = Vehiculo.objects.values_list('marca', flat=True).distinct()
    colores = Vehiculo.objects.values_list('color', flat=True).distinct()
    
    context = {
        'vehiculos': vehiculos,
        'marcas': marcas,
        'colores': colores,
    }
    return render(request, 'vehiculos_listar.html', context)

# --------------------------------------------------------------------------------

def propietariosListar(request):
    propietarios = Propietario.objects.all()
    
    # Filtros
    search = request.GET.get('search', '')
    if search:
        propietarios = propietarios.filter(
            Q(nombre__icontains=search) |
            Q(apPaterno__icontains=search) |
            Q(RFC__icontains=search) |
            Q(CURP__icontains=search)
        )
    
    municipio = request.GET.get('municipio', '')
    if municipio:
        propietarios = propietarios.filter(municipio=municipio)
    
    municipios_list = Propietario.objects.values_list('municipio', flat=True).distinct()
    
    return render(request, 'propietarios_list.html', {
        'propietarios': propietarios,
        'municipios': municipios_list
    })

def propietariosCrear(request):
    if request.method == 'POST':
        form = PropietarioForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('propietariosListar')
    else:
        form = PropietarioForm()
    return render (request, 'propietarios_crear.html', {'form':form}) 

def propietariosEditar(request, id):
    propietario = Propietario.objects.get(id=id)
    if request.method == 'GET': # Cuando se ingresa a editar. Se pinta con los datos del registro apropiado
        form = PropietarioForm(instance = propietario)     # Pinta form lleno
    else:   # Ya se modificio el registro
        form = PropietarioForm(request.POST, instance=propietario) #Modificado 
        if form.is_valid():
            form.save()                                    # Lo guarda 
        return redirect ('propietariosListar') 
    
    return render (request, 'propietarios_crear.html', {'form':form})

def propietariosEliminar(request, pk):
    propietario = Propietario.objects.get(pk=pk)
    if request.method == 'POST':            # Se confirma eliminar
        propietario.delete()                    # Se borra registro de la BD
        return redirect('propietariosListar')   # Se redirecciona al listado
    
    return render (request, 'propietarios_eliminar.html', {'propietario':propietario}) 

def vehiculosCrear(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculosListar')
    else:
        form = VehiculoForm()
    return render (request, 'vehiculos_crear.html',{'form':form})
    
def vehiculosDelete(request):
    pass 

def vehiculosUpdate(request):
    pass

from django.db.models import Count  # AGREGAR ESTA IMPORT

def estadisticas(request):
    total_vehiculos = Vehiculo.objects.count()
    total_propietarios = Propietario.objects.count()
    total_oficinas = Oficina.objects.filter(activa=True).count()
    
    vehiculos_por_marca = Vehiculo.objects.values('marca').annotate(
        total=Count('id')
    ).order_by('-total')
    
    propietarios_por_municipio = Propietario.objects.values('municipio').annotate(
        total=Count('id')
    ).order_by('-total')[:5]
    
    # Agregar estos para la información del sistema
    vehiculos = Vehiculo.objects.all().order_by('-fecha_registro')
    propietarios = Propietario.objects.all().order_by('-fecha_registro')
    
    context = {
        'total_vehiculos': total_vehiculos,
        'total_propietarios': total_propietarios,
        'total_oficinas': total_oficinas,
        'vehiculos_por_marca': list(vehiculos_por_marca),
        'propietarios_por_municipio': list(propietarios_por_municipio),
        'vehiculos': vehiculos,
        'propietarios': propietarios,
    }
    return render(request, 'estadisticas.html', context)