# Listas

lista = ['Lunes', 'Martes', 'Miercoles', 'Jueves',
         'Viernes', ['mañana', 'tarde', 'noche']]

print(lista)
print(lista[1])
print(lista[-1])

print(lista[0:3])  # Sublista

print(len(lista))

# Methods

lista2 = [1, 2, 4, 5, 'juanka']

lista2.append(6) # add end of the list
lista2.pop() # delete element of the list by index
lista2.remove(5) # delete element of the list by value
lista2.clear() # delete all elements of the list
lista2.reverse() # reverse all elements of the list
lista2.sort() # order list
lista2.insert(2, 3)  # (index, value)
lista2.extend([7, 8, 9])  # combinar lista
lista2.index(2) # index 
lista2.count(2) # cuantas veces se repite en una lista 
print( 'juanka' in lista2) # buscar en lista
# lista3 = lista + lista2

print(lista2)

