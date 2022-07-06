import json

filename = open("empleados.txt")
diccionario = []

for line in filename:
    pipe_split = {ele.strip() for ele in line.split(",")}
    line_dict = dict()
    for ele in pipe_split:
        key, val = ele.split(":", 1)
        line_dict[key] = val
    diccionario.append(line_dict)

with open("empleados.json", "w") as f:
    json.dump(diccionario, f, indent=4)
