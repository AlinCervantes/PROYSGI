from django.urls import path

from usuarios import views

urlpatterns = [
    path('home/',views.homeUsuarios, name='homeUsuarios'),

]