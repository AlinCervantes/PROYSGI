import os
os.system('cls')

conjunto1 = set()
conjunto1.add(10)
# conjunto1.add(2,3) Error
print(conjunto1)
conjunto1.add('Hola')
print(conjunto1)

conjunto2 = conjunto1.copy()
print(conjunto2)

conjunto2.add(20)
print(conjunto1)
print(conjunto2)
print('Diferencia de c1 con c2',conjunto1.difference(conjunto2))
print('Diferencia de c2 con c1',conjunto2.difference(conjunto1))
input()
conjunto2.discard(20)
print(conjunto2)

conjunto1.add('aa')
conjunto2.add(30)
print('\nCONJUNTO1: ', conjunto1)
print('CONJUNTO2: ', conjunto2)
print('Intersección: ', conjunto1.intersection(conjunto2))

print('\nSon diferentes los conjuntos?: ', conjunto1.isdisjoint(conjunto2))

conjuntoA= set([1, 2, 3])
conjuntoB= set([4, 5, 6])
print('\nEstos conjuntos son diferentes?: ', conjuntoA.isdisjoint(conjuntoB))

conjunto1= set([2, 3])
conjunto2= set([1, 2, 3, 4, 5, 6])
print('\nCONJUNTO1: ', conjunto1)
print('CONJUNTO2: ', conjunto2)
print('El primer conjunto es subconjunto del segundo:? ', conjunto1.issubset(conjunto2))
print('El primer conjunto es superconjunto del segundo:? ', conjunto1.issuperset(conjunto2))
print('El segundo conjunto es superconjunto del primero:? ', conjunto2.issuperset(conjunto1))

print('\nValor devuelto al eliminar con pop(): ', conjunto2.pop()) #Generalmente es el primer elemento 
print(conjunto2)

conjunto2.remove(6) # Elimina el valor especificado como argumento
print(conjunto2)

conjunto1 = set([2, 4, 6, 8])
conjunto2 = set([1, 3, 5, 7, 9])
conjuntounion = conjunto1.union(conjunto2)
print('\nCONJUNTO1: ', conjunto1)
print('CONJUNTO2: ', conjunto2)
print('Conjunto Union: ',conjuntounion)

conjunto1.clear()
print('\n',conjunto1)

