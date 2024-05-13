def beolvas(filename):
    f = open(filename, "r", encoding="utf-8")
    rows = f.readlines()
    lista = []
    for i in range(len(rows)):
        rows[i] = rows[i].strip()
        lista.append(rows[i].split())
    for i in range(len(lista)):
        for x in range(1, len(lista[i])):
            lista[i][x] = int(lista[i][x])
    return lista
lista = beolvas("24_5_13/file.txt")
osszeg = 0
for i in range(1, len(lista[1])):
    osszeg += lista[1][i]
print(lista)
print(f'Dóra összeg: {osszeg}')