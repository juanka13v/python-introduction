# Argumentos y parametros

def resta(num1,num2):
    return num1-num2

print(resta(4,3))
print(resta(num2=4,num1=3))


# Argumentos por valor o por referencia

def doblar_valor(numero):
    numero *= 2
    print(numero)

n = 5

doblar_valor(n)

print(n)