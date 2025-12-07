matr = ([0,0,0],[0,0,0],[0,0,0])

for i in range(3):
    for j in range (3):
        #dato= int(input('Valor: '))
        #matr[i][j] = dato
        matr[i][j] = int(input('Valor [{0}] [{1}]: '.format(i,j)))
        
sumatotal=0        
for i in range(3):
    sumafila=0
    for j in range (3):
        print(matr[i][j])
        sumafila+= matr[i][j]
    print('Suma de fila= ', sumafila)
    sumatotal+= sumafila

