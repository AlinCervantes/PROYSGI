################Operaciones que hara nuestro codigo###########
#Agregar un contacto
#Borrar contacto
#Actualizar contacto
#Ver contacto
#Ver todos los contactos
 
#creamos nuestro diccionario
agenda = dict()
#Funciones para nuestra agenda
def agregar_contacto():
	print ("*** AGREGAR CONTACTO ***\n")
	nombre = input("Nombre del contacto: ")
	#comprbamos si el contacto ya existe
	if nombre.capitalize() in agenda:
		print ("¡¡¡¡ EL CONTACTO YA EXITE !!!!")
		nombre = input("Nombre del contacto: ")
		if nombre.capitalize() not in agenda:
			numero = input("Numero del contacto: ")
			agenda[nombre.capitalize()]= numero
	else:
		numero = input("Numero del contacto: ")
		agenda[nombre.capitalize()]= numero
	print()
 
def borrar_contacto():
	print ("*** BORRAR CONTACTO ***\n")
	nombre = input ("Nombre del contacto que deseas borrar: ")
#para prevenir un keyerror en caso que el nombre no existe creamos un Try
	try:
		del agenda[nombre.capitalize()]
		print()
		print("----Registro eliminado----\n")
	except KeyError:
		#print()
		print("El registro que estas intentando eliminar no existe \n")
 
 
def actualizar_contacto():
	print ("*** ACTUALIZAR CONTACTO ***\n")
	nombre = input("Nombre del contacto: ")
	#comprobamos si el nombre que se desea actualizar existe en nuestro diccionario
	#si existe actualizamos el numero, si no existe mandamos el mensaje
	if nombre.capitalize() in agenda:
		#elimino el registro previo del contacto a atualizar, una vez comprado que existe y pido
		del agenda[nombre.capitalize()]
		#pido los nuevos valores del contacto
		nombre = input("Actualizar nombre de contacto: ")
		numero = input("Actualizar numero del contacto: ")
		agenda[nombre.capitalize()] = numero
		print("----Contacto actualizado----\n")
	else:
		print("El registro que deseas actualizar no existe\n")
 
 
def ver_contacto():
	print ("*** VER CONTACTO ***\n")
	nombre = input("Que contacto deseas ver: ".capitalize())
	try:
		print(nombre.capitalize(), "-",agenda[nombre.capitalize()])
		print()
	except KeyError:
		print("El contacto que deseas visualizar no existe\n")
 
def listar_cotactos():
	print ("*** LISTAR CONTACTOs ***\n")
	#creamos un fin con un len, y comprobamos si el diccionario es == 0 entonces 
	#no hay nada que mostrar y desplegamos un mensaje
	if len(agenda) == 0:
		print("Tu agenda esta vacia\n")
	#key lo tomo como un "identificador", key regresa el nombre de las llaves(no es necesario)
	#que lleve como nombre "key" puede ser cualquier otra variable. Despues ponemos el nombre
	#del diccionario, en este caso "agenda", y ponemos dentro [] de nuevo la variable key, para
	#que nos regrese el valor de "key" ( o nuestra variable ). Es decir si agrego como nombre en el 
	#diccionario a Ricardo con el valor de 312000000, lo que hacemos con el ciclo for es 
	#devolver en primer lugar el nombre(Ricardo con la variable "key") y despues el valor
	#de nuestra variable 312000000 (utilizando el diccionario y pasando "key", para retonar el valor)
	for key in agenda:
		print(key, "-",agenda[key])
	print()
 
print("****** Bienvenidos a contactos 1.0 ******".upper())
print()
while True:
	try:
		print("1.- AGREGAR CONTACTO")
		print("2.- VER CONTACTO")
		print("3.- LISTAR CONTACTOS")
		print("4.- ACTUALIZAR CONTACTO")
		print("5.- BORRAR CONTACTO")
		print("6.- SALIR")
		print()
		opcion = int(input("Que accion deseas realizar? "))
		print()
	except ValueError:
		print("¡¡¡¡ FAVOR DE AGREGAR SOLO NUMEROS !!!\n")
	else:
		if opcion < 1 or opcion > 6:
			print ("¡¡¡ NO ES UNA OPCION VALIDA !!!\n")
			continue
		if opcion == 1:
			agregar_contacto()
		elif opcion == 2:
			ver_contacto()
		elif opcion == 3:
			listar_cotactos()
		elif opcion == 4:
			actualizar_contacto()
		elif opcion == 5:
			borrar_contacto()
		else:
			break
print("*** GRACIAS POR UTILIZAR AGENDA 1.0 ***")
print("----------- HASTA LA PROXIMA ----------")
print("*** *** *** *** *** *** *** *** *** ***\n")
