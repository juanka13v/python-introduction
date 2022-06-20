# Funciones sin retorno de valor

def saludar():
    print("Hola amigo")


saludar()


def saludar2(nombre):
    print(f"Hola {nombre}")


saludar2("juanka")


def tabla_multiplicar(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


tabla_multiplicar(5)


# Funciones con retorno de valor

def multiplicar(num1, num2):
    mult = num1*num2
    return mult

print(multiplicar(5,3))