# cadenas de caracteres


cadena = 'Hola \t Mundo' # tabulacion
cadena = 'Hola \n Mundo' # salto de linea

cadena = r'D:\nombre\trabajos' # row
cadena = """-LINEA A 
-LINEA B
-LINEA D
""" # texto en varias lineas


print(cadena)

# indices y slicing

string = "juanka"


print(string[2])
print(string[-2])
print(string[1:4])

# metodos

cadena = 'Hola mundo'

print(cadena.upper()) 
print(cadena.lower()) 
print(cadena.capitalize()) 
print(cadena.title()) 
print(cadena.count('o')) 
print(cadena.find('o')) # index 
print(cadena.rfind('o')) # last coindice 
print(cadena.isdigit())
print(cadena.isalpha()) # comprueba valores alfabeticos
print(cadena.isalnum()) #alphanumericos
print(cadena.islower())
print(cadena.isupper())
print(cadena.istitle())
print(cadena.isspace())

print(cadena.startswith('hola'))
print(cadena.endswith('o'))
print(cadena.split())
print("-".join(cadena))
print(cadena.strip())
print(cadena.replace('hola',"Hola"))

