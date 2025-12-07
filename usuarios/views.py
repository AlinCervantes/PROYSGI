from django.shortcuts import render

# Create your views here.
def homeUsuarios(request):
    return render (request, 'homeUsuarios.html')

