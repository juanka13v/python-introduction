# Bucle for
'''
coleccion = ['a', 'b', 'c', 'd', 'e']

for i in coleccion:
    print(i)

diccionario = {'juan': 23, 'mario': 15, "monica": 21}

for clave, valor in diccionario.items():
    print(f"{clave} -> {valor}")

nombre = 'juanka'

for i in nombre:
    print(f"{i}", end=" ")
'''

# Bucle for tipo range


from winreg import REG_NO_LAZY_FLUSH


for i in range(10):
    print(i)

for i in range(5,11): # rango de 5 a 10
    print(i)

for i in range(2,21,2): # salta de dos en dos
    print(i)


# Instruccion continue y break

for i in range(10):
    if i == 5:
        continue
    print(i)

for i in range(10):
    if i == 5:
        break
    print(i)