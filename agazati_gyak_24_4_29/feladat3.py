def adatbeolvasás(filename):
    f = open(filename, encoding="utf-8")
    rows = f.readlines()
    f.close()
    lista = []
    for i in range(len(rows)):
        rows[i] = rows[i].strip()
        lista.append(rows[i].split())
    for i in range(len(lista)):
        for x in range(1, len(lista[i])):
                lista[i][x] = int(lista[i][x])
    return lista
def nullaKm(lista):
    count = 0
    for i in range(len(lista)):
        for x in range(1, len(lista[i])):
            if lista[i][x] == 0:
                count += 1
    return count
lista = adatbeolvasás('agazati_gyak_24_4_29/fuvarok.txt')
print(f'Az adatbázisban {nullaKm(lista)}db 0km havi futásteljesítményt tartalmazó hónap van.')