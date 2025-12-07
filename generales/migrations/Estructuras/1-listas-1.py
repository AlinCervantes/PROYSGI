''' LISTAS: 
En Python las listas son uno de los tipos de básicos de variables u objetos. 
Para generar una lista basta hacer una asignación a un nombre de variable 
con los elementos dentro de corchetes cuadrados [ ] 
'''


L1 = [1,2,3,4,5,'A', 'B','C']
print(type(L1))
print (L1)                      #Imprime toda la lista
input("\n Presiona <<Enter>> para continuar...")

print ("Impresion de cada elemento de la lista, segun su indice")
for i in range(len(L1)):
    print (L1[i])               # Imprime cada elemento de la lista
input("\n Presiona <<Enter>> para continuar...")

print ("Visualización de la lista despues de agregar elementos... ")
L1.extend([10,11])              #Funcion agregar al final de la lista
print (L1)
input("\n Presiona <<Enter>> para continuar...")

print ("Visualización de un rango de la lista... ")
print (L1[0:5])                 #Imprime lista en el rango de indices 0..5
input("\n Presiona <<Enter>> para continuar...")

print ("Otra forma de imprimir por rangos ... ")
print (L1[:5])                  #Imprime lista en el rango de indices 0..5
input("\n Presiona <<Enter>> para continuar...")
print (L1[5:])                  #Imprime lista en el rango de indices 5: a len de L1



print ("\n\nAhora se generará una nueva lista vacia y se agregarán los elementos al final de la misma... ")
l2 = []

for i in range(3):
    dato= int(input("Introduce un valor: "))
    l2.extend([dato])

print (l2)