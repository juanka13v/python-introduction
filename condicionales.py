# condicionales

numero = int(input('Escribe un Numero: '))

if numero > 0:
    print('Es un numero positivo')
elif numero == 0:
    print('Es un numero cero')
else:
    print('Es un numero negativo')

print('Fin del Programa')

# condicionales combinadas

edad = int(input('Digite su edad: '))

if edad > 0 and edad < 100:
    print('Edad correcta')
    if edad >= 18:
        print('Es mayor de edad')
    else:
        print('No es mayor de edad')
else:
    print('Edad incorrecta')
