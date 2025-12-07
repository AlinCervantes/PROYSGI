romanos =  dict()

romanos = { 1 : 'I', 
            2 : 'II', 
            3 : 'III',
            4 : 'IV', 
            5 : 'V', 
            6 : 'VI',
            7 : 'VII',
            8 : 'VIII',
            9 : 'IX',
            10 : 'X'}
            
print (romanos)

# Recorrer un diccionario, imprimiendo su clave-valor
for k,v in romanos.items():
    print ("{0} -> {1}".format(k,v))

print()

# Devuelve el numero de elementos que tiene el diccionario
print ('Numero de elementos', len(romanos))

print()

# Devuelve una lista con las claves del diccionario
print('Claves en el diccionario: ', romanos.keys())

print()

# Devuelve una lista con los valores del diccionario
print('Valores en el diccionario: ', romanos.values())

print()

# Devuelve el valor del elemento con clave <especifica>. Sino devuelve default
valor = romanos.get(3)
print ('>>', valor)

print()

# Inserta un elemento en el diccionario clave:valor. Si la clave existe no lo inserta
romanos.setdefault(1 , 'Nuevo')
print(romanos)
#No se inserta el valor 'Nuevo' porque la clave 1 ya existe con el valor 'I'

print()

romanos.setdefault(11 , 'XI')
print(romanos)
# Ahora existe el par 11:'XI' ya que esa clave no estaba dada de alta

print()

# Eliminamos el elemento del diccionario con clave key
romanos.pop(11)
print(romanos) # Ya no existe el par 11:'XI'

print()

# Insertamos un elemento en el diccionario con su clave:valor
romanos[1] = 'Nuevo valor'
print(romanos)
#Se permite el cambio de la clave 1 con el valor 'Nuevo valor'

print()

# devuelve un lista de tuplas formadas por los pares clave:valor
print(romanos.items())

