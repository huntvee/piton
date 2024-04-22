filename="input4.txt"
file=open(filename, "r", encoding="UTF-8")
sorok = file.readlines()
file.close()
print(sorok)
lista = []
for i in range(len(sorok)):
    sorok[i] = sorok[i].strip()
    lista.append(sorok[i].split(';'))
for i in range(len(lista)):
    if i >= 1:
        for x in range(1, len(lista[i])):
            lista[i][x] = int(lista[i][x])
print(lista)