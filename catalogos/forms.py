from django import forms 
from .models import Oficina, Vehiculo, Propietario

class OficinaForm(forms.ModelForm):
    class Meta:
        model = Oficina
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})
            

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class' : 'form-control'})
    
    '''
    class meta:
        model = Vehiculo
        fields = [
            'NIV',
            'noMotor',
            'marca',
            'linea',
            'modelo'
        ]
    ''' 