def adatbeolvasás(filename):
    f = open(filename, encoding="utf-8")
    rows = f.readlines()
    f.close()
    lista = []
    for i in range(len(rows)):
        rows[i] = rows[i].strip()
        lista.append(rows[i].split())
    for i in range(len(lista)):
        for x in range(len(lista[i])):
                lista[i][x] = int(lista[i][x])
    return lista
def hatékonyság(lista):
    count = 0
    hatekonynap = 0
    for i in range(len(lista)):
        for x in range(1, len(lista[i])):
            if lista[i][x] == 0:
                count += 1
        if count >= 3:
             hatekonynap +=1
             count = 0
    return hatekonynap
lista = adatbeolvasás('agazati_gyak_24_4_29/adat.txt')
print(lista)
print(f'Hatékony napok száma: {hatékonyság(lista)}')