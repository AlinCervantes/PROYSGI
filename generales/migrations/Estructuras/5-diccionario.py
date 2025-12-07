import os

alumnos =  dict()

alumnos = { 1 : 'Antonio', 2 : 'Joel', 3 : 'Maria', 4 : 'Roberto', 5 : 'Ana', 6 : 'Laura'}
print (alumnos)
 
input("Presiona enter>> ")
os.system("cls")

# Recorrer un diccionario, imprimiendo su clave-valor
for clave,valor in alumnos.items():
    print ("{0} -> {1}".format(clave,valor))

# Devuelve el numero de elementos que tiene el diccionario
print ('Numero de elementos', len(alumnos))

# Devuelve una lista con las claves del diccionario
print('Claves en el diccionario: ', alumnos.keys())

# Devuelve una lista con los valores del diccionario
print('Valores en el diccionario: ', alumnos.values())

# Devuelve el valor del elemento con clave <especifica>. Sino devuelve default
clave = alumnos.get(3)
print ('>>', clave)

# Inserta un elemento en el diccionario clave:valor. Si la clave existe no lo inserta
alumnos.setdefault(1 , 'Nuevo')
print(alumnos)

alumnos.setdefault(7 , 'Nuevo')
print(alumnos)

# Eliminamos el elemento del diccionario con clave key
alumnos.pop(7)
print(alumnos)

# Insertamos un elemento en el diccionario con su clave:valor
alumnos[1] = 'Nuevo valor'
print(alumnos)

# Devuelve true si existe la clave. Si no devuelve false
#existe1 = alumnos.has_key(1)
#print('Alumno con clave 1 = ', exist1)

# devuelve un lista de tuplas formadas por los pares clave:valor
print(alumnos.items())

