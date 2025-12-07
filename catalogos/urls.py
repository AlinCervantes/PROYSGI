from django.urls import path

from catalogos import views

urlpatterns = [
    path('home/',views.homeCatalogos, name='homeCatalogos'),
    
    path('oficinas/listar',views.oficinaListar, name='oficinasListar'),
    path('oficinas/crear',views.oficinasCrear, name='oficinasCrear'),
    path('oficinas/editar/<int:id>/', views.oficinasEditar, name='oficinasEditar'),
    path('oficinas/eliminar/<int:pk>/', views.oficinasEliminar, name='oficinasEliminar'),
    
    path('vehiculos/listar/',views.vehiculosListar, name='vehiculosListar'),
    path('vehiculos/crear/', views.vehiculosCrear, name='vehiculosCrear'),
    path('vehiculos/delete/', views.vehiculosDelete, name='vehiculosDelete'),
    path('vehiculos/update/', views.vehiculosUpdate, name='vehiculosUpdate'),
    
    path('propietarios/listar', views.propietariosListar, name='propietariosListar'),
    path('propietarios/crear', views.propietariosCrear, name='propietariosCrear'), 
    path('propietarios/editar/<int:id>', views.propietariosEditar, name='propietariosEditar'),
    path('propietarios/eliminar/<int:pk>', views.propietariosEliminar, name='propietariosEliminar'),

]