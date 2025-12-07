class Pila:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def incluir(self, item):
        self.items.append(item)

    def extraer(self):
        if p.longitud() == 0 : 
            print ('La lista está vacía') 
        else:
            print('Elemento eliminado de la pila: ', self.items[len(self.items)-1])
            return self.items.pop()

    def ultimo(self):
        if p.longitud() == 0 : 
            print ('La lista está vacía') 
        else:
            return self.items[len(self.items)-1]

    def longitud(self):
        return len(self.items)

    def recorrer (self):
        for i in self.items:
            print('  ',i) 

    def mostrar_tope(self):
        if p.longitud() == 0 : 
            print ('La lista está vacía') 
        else:
            print ('Elemento en tope de pila:\n', p.ultimo())


p=Pila()
p.mostrar_tope()
input()

p.extraer()

p.ultimo()
input()

p.recorrer()
input()

p.incluir(4)
p.mostrar_tope()
input()

p.incluir('perro')
p.mostrar_tope()

p.incluir('gato')
p.mostrar_tope()

print('Pila completa: ')
p.recorrer()

p.extraer()
print('Se ha elminado elemento de la pila')
input()

print('Pila completa: ')
p.recorrer()