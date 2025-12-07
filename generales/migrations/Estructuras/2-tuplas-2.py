T = ("Masculino", "Femenino")
genero1, genero2 = T
print (genero1)  # Se imprime “Masculino”
print (genero2)  # Se imprime “Femenino”

input()

valores = ("Python", True, 3.1416, 5, "Python")
print ("True ->", valores.count(True))
print ("3.1416 ->", valores.count(3.1416))
print ("Python ->", valores.count("Python"))

print (valores.index(True)) # Esta en el indice 1
print (valores.index(5)) # Esta en el indice 3

L = ['a', 'e', 'i', 'o', 'u']   # L es una lista de 5 elementos
print (type(L))                 # Se imprime list()
print (L)                       # Se imprime el contenido de la lista L
T = tuple (L)                   # Se convierte L a una tupla y se almacena en T
print (type(T))                 # Se imprime tuple()
print (T)                       # Se imprime el contenido de T = ('a', 'e', 'i', 'o', 'u')




