#1 feladat, fajl megnyitasa
file = open("korep/input.txt", encoding='utf-8')
sorok = file.readlines()
file.close()
lista = []
#beolvasas, listaba helyezes
for i in range(1,len(sorok)-1):
    templista=sorok[i].strip()
    lista_parts=templista.split()
    _l=[]
    for j in range(len(lista_parts)):
        _l.append(int(lista_parts[j]))
    lista.append(_l)
print (lista)
#2 feladat
osszeg = 0
sorosszeg = 0
for i in range(len(lista)):
    for j in range(len(lista[i])):
        osszeg += lista[i][j]
        sorosszeg += lista[i][j]
    print(f'Az {i+1} sor osszege: {sorosszeg}')
print(f'A fajl osszege: {osszeg}')
#3 feladat
szam = int(input('Adj meg egy szamot: '))
darab = 0
van = None
for i in range(len(lista)):
    for j in range(len(lista[i])):
        if szam == lista[i][j]:
            van = True
            darab += 1
if van:
    print(f'A keresett szam: {szam}. A szambol {darab} van a listaban.')
else:
    print('A szam nincs benne a listaban.')
#4 feladat
paros = 0
paratlan = 0
for i in range(len(lista)):
    for j in range(len(lista[i])):
        if lista[i][j]%2==0:
            paros +=1
        else:
            paratlan +=1
print (f'Paros szamok: {paros}. Paratlan szamok: {paratlan}.')
#5 feladat
sor = 0
hely = 0
maxszam = 0
for i in range(len(lista)):
    for j in range(len(lista[i])):
        if lista[i][j] >= maxszam:
            maxszam = lista[i][j]
            sor = i+1
            hely = j+1
print(f'A legnagyobb szam: {maxszam}. Helye: {sor}. sor, {hely}. szam.')