lista=[]

for i in range (5):
    dato = int(input('Valor {0}: '.format(i)))
    lista.extend ([dato])

print('\nCONTENIDO DE LA LISTA: ')
for i in range (len(lista)):
    print (lista[i])

