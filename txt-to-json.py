import json

#Convertir el txt a lista
filename = "empleados.txt"
with open(filename) as file:
    for line in file:
        data = list(line.strip().split(None, 4))
        print(data)

description = ['firstname', 'surname', 'country', 'language', 'airport']

#Fusionar ambas listas en un diccionario (lista del txt y lista de las descripciones)
outputData = {description[i]:data[i] for i in range(len(data))}
with open('formato_resultante.json', 'a') as file2:
    json.dump(outputData, file2)