nombres = []
c1 = []
c2 = []
c3 = []
prom = []

for i in range (3):
    dato = input('Nombre {0}: '.format(i))
    nombres.extend ([dato])

print ('CALIFICACIONES DEL PARCIAL 1: ')
for i in range (3):
    dato = int(input('{0}: '.format(nombres[i])))
    c1.extend ([dato])

print ('CALIFICACIONES DEL PARCIAL 2: ')
for i in range (3):
    dato = int(input('{0}: '.format(nombres[i])))
    c2.extend ([dato])

print ('CALIFICACIONES DEL PARCIAL 3: ')
for i in range (3):
    dato = int(input('{0}: '.format(nombres[i])))
    c3.extend ([dato])

for i in range (3):
    p = (c1[i] + c2[i] + c3[i]) / 3 
    prom.extend ([p])

print('\nNombre\tParcial1\tParcial2\tParcial3\tPromedio')
for i in range (3):
    print(nombres[i], '\t', c1[i], '\t\t', c2[i], '\t\t', c3[i], '\t\t', prom[i]) 

'''
for i in range (3):
    print ('{0} \t {1} \t {2} \t {3} \t {4}'.format(nombres[i], c1[i], c2[i], c3[i], prom[i}]))
'''