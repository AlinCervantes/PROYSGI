''' TUPLAS:
La TUPLA es otro tipo de arreglo que dispone el Python. Esta variable está 
más cerca al concepto matemático de vector, puesto que en Python la tupla 
se maneja como una lista más cerrada porque no puede cambiar elementos individuales, 
en otras palabras, es inmutable según lo definen los manuales 
'''
a = 1, 3, 5, 5
b = (['1','2','3'], 'bbb', 'cccc', 1, 2, 3, 4)
c = ([1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15])

print (type(a))
input()
print (a)
input()
print (b)
input()
print (c)

# a[0]= 9      # Provoca un error porque no se pueden reasignar valores a la tupla  

for i in range(0,len(a)):
    print(a[i])

for i in range(len(b)):
    print (b[i])

for i in range(len(c)):
    print (c[i])

d= list(a)
print('Ahora es una lista: ', d)
d[0] = 0
print('Lista modificada: ', d)
d.extend([7,9])
d[0]= 1
print ('Mas modificada: ', d)
a= tuple(d)
print(a)
print (type(a))

print (a.count(5))

#indice
print(a.index(3))

