from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    NIV = models.CharField(max_length=20, null=False, help_text="NIV del vehiculo")
    noMotor = models.CharField(max_length=30, blank=True)
    marca = models.CharField(max_length=40)
    linea= models.CharField(max_length=40)
    modelo= models.CharField(max_length=4)
    
    def __str__(self):
        return '%s - %s - %s' % (self.NIV, self.marca, self.linea)
    
    """def __save__(self):
        self.NIV = self.NIV.upper()
        self.noMotor = self.noMotor.upper()
        super(Vehiculo, self.save())"""
    
    def save(self, *args, **kwargs):  # Cambia __save__ por save
        self.NIV = self.NIV.upper()
        if self.noMotor:
            self.noMotor = self.noMotor.upper()
        super().save(*args, **kwargs)
    
    class Meta:  # NO class meta
        verbose_name_plural = "Vehiculos"  # Opcional cambiar nombre
        db_table = 'vehiculos'  # Opcional cambiar nombre tabla
        
class Propietario(models.Model):
    RFC = models.CharField(max_length=50)
    nombre = models.CharField(max_length=30)
    apPaterno = models.CharField(max_length=30)
    apMaterno = models.CharField(max_length=30)
    email = models.EmailField()
    CURP = models.CharField(max_length=14)
    calle = models.CharField(max_length=50)
    colonia = models.CharField(max_length=40)
    municipio = models.CharField(max_length=40)
    CP = models.CharField(max_length=5)
    edad = models.IntegerField(default=0)
    
    def __str__(self):
        return '%s - %s - %s' % (self.nombre, self.apPaterno, self.apMaterno)
    
    '''
    def __save__(self):
        self.CURP = self.CURP.upper()
        super(Propietario,self).save()
    '''

    def save(self, *args, **kwargs):  # Cambia __save__ por save
        self.CURP = self.CURP.upper()
        super().save(*args, **kwargs)
            
class Oficina(models.Model):
    nombre = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    telefono = models.CharField(max_length=10)
    
    def __str__(self):
        return "%s" % (self.nombre)
        
class Placa(models.Model):
    numero = models.CharField(max_length=10)
    numTC = models.CharField(max_length=20)
    fecha = models.DateField(auto_now_add=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    estatus = models.BooleanField(default=True)
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s - %s" % (self.numero, self.vehiculo)
    