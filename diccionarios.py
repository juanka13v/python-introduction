# Diccionarios | <clave>:<valor>

diccionario = {"azul": "blue", "rojo": "red", "verde": "green"}

print(diccionario["azul"])

diccionario["amarrillo"] = "yellow"  # add
diccionario["azul"] = "sea"  # change
del(diccionario["azul"])  # delete

print(diccionario)

equipo = {
    10: "paulo",
    11: "cristiano",
    7: "jorge",
    17: "maria",
}

print(equipo.items())
print(equipo.keys())
print(equipo.values())
print(equipo.get(19, "No existe esa clave"))
print(equipo)
