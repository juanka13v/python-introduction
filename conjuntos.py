'''
#conjuntos
    son desordenados
    no pueden tener valores repetidos
    no pueden contener una lista, tupla
'''


conjunto = set()
# or
conjunto = {'red', 'blue', 'green'}

conjunto.add('orange')
conjunto.add('black')
conjunto.add('gray')

conjunto.discard('gray')  # delete a value

conjunto.clear()  # delete all values

print(conjunto)

# operaciones

a = {1, 2, 3}
b = {3, 4, 5}

c = a | b  # unir conjuntos
c = a & b  # inter conjuntos
c = a - b  # diferencia conjuntos
c = a ^ b  # diferencia simetrica conjuntos

c = {1,2,3,4,5}
print(a.issubset(c)) # subconjunto
print(c.issubset(a)) # superconjunto
print(a.isdisjoint(b)) # disconexos

d = frozenset({1,2,3,4}) # es inmutable

print(c)
