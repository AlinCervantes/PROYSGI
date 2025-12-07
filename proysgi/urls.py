from django.contrib import admin
from django.urls import path, include

from generales import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    
    # Rutas que se resuelven en otra ubicacion (Una App)
    path('catalogos/', include('catalogos.urls')),
    path('usuarios/', include('usuarios.urls')), 
]
