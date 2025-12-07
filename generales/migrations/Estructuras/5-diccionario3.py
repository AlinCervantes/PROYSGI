alumnos =  dict()
alumnos = { 1 : 'Antonio', 2 : 'Joel', 3 : 'Maria',
            4 : 'Roberto', 5 : 'Ana', 6 : 'Laura'}
            
for k,v in alumnos.items():
    print ("{0} -> {1}".format(k,v))

print ('Numero de elementos', len(alumnos))
print('Claves en el diccionario: ', alumnos.keys())
print('Valores en el diccionario: ', alumnos.values())

valor = alumnos.get(3)
print ('>>', valor)

alumnos.setdefault(1 , 'Nuevo')
print(alumnos)
alumnos.setdefault(7 , 'Nuevo')
print(alumnos)
alumnos.pop(7)
print(alumnos)
alumnos[1] = 'Nuevo valor'
print(alumnos)
print(alumnos.items())

