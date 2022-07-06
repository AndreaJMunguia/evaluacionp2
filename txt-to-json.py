import json

filename = open("empleados.txt")
lista = []

for line in filename:
    split = {i.strip() for i in line.split(",")}
    line = dict()
    for i in split:
        key, valor = i.split(":", 1)
        line[key] = valor
    lista.append(line)

with open("empleados.json", "w") as f:
    json.dump(lista, f, indent=4)
