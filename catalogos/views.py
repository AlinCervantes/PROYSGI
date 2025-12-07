from django.shortcuts import render, HttpResponse, redirect
from .models import Oficina, Vehiculo, Propietario
from .forms import OficinaForm, VehiculoForm, PropietarioForm

# Create your views here.
def homeCatalogos(request):
    return render(
        request,
        'homeCatalogos.html'
    )
    
def oficinaListar(request):
    oficinas = Oficina.objects.all()
    data = {'oficinas' : oficinas}
    return render (request,'oficinas_listar.html', data)

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
    datos = {'vehiculos' : vehiculos}
    return render (request, 'vehiculos_listar.html', datos)

# --------------------------------------------------------------------------------

def propietariosListar(request):
    propietarios = Propietario.objects.all() #se obtienen los registros de la bd
    data = {'propietarios' : propietarios}   #se construye dict de datos
    return render (request, 'propietarios_list.html', data)

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
