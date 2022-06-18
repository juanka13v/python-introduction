from cgi import print_directory


print('Hola Mundo')
print('Hola Mundo 3')
print('Hola Mundo\nmi nombre es juanka')

# Variables

numero = 10  # int
numero_float = 10.14  # float
cadena = 'juanka'  # string
valor = True  # boolean

print(type(numero))
print(type(numero_float))
print(type(cadena))
print(type(valor))


# operations aricmeticas

num1 = 10
num2 = 2
suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
div = num1 / num2
div_exacta = num1 // num2
modulo = num1 % num2
potencia = num1 ** num2


print('La suma es: ', suma)
print('La resta es: ', resta)
print('El producto es: ', mult)
print('La division es: ', div)
print('El modulo es: ', modulo)
print('La potencia es: ', potencia)

# operadores relacionales

op1 = num1 > num2
op2 = num1 < num2
op3 = num1 >= num2
op4 = num1 <= num2
op5 = num1 == num2
op6 = num1 != num2

print(op1)
print(op2)
print(op3)
print(op4)
print(op5)
print(op6)

# Operadores Logicos

a = 10
b = 12
c = 13
d = 10

print(((a > b) or (a < c)) and ((a == c) or (a >= b)))


# Operadores de Asignacion

a = 0

a += 5  # Suma en asignacion
print(a)
a -= 2  # Resta en asignacion
print(a)
a *= 3  # multiplicacion en asignacion
print(a)
a /= 3  # division en asignacion
print(a)
a **= 2  # potencia en asignacion
print(a)
a %= 2  # modulo en asignacion
print(a)

# Salidas

nombre = 'juanka'
edad = 22

print("Hola", nombre, 'tienes', edad, 'años')

print("Hola {} tienes {} años".format(nombre, edad))

print(f"Hola {nombre} tienes {edad} años")

# Entrada de datos

# name = input('Digite su nombre: ')
number = int(input('Digite un numero: '))

# print(f"Hola {nombre}")
print(f"El numero es {number}")