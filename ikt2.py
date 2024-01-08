import random
#1 feladat
elemszam = 0
while elemszam > 60 or 30 > elemszam:
    elemszam = int(input('Add meg a lista elemszámát [30...60]:'))
    if elemszam > 60 or 30 > elemszam:
        print('Hibás adatbevitel! Próbáld meg újra...')
lista = []
for i in range(elemszam):
    lista.append(random.randint(-100, 100))
#2 feladat
kezdo = 0
bef = 0
while True:
    kezdo = int(input(f'Add meg a kezdő sorszámot [1...{elemszam}]:'))
    if 1 <= kezdo <= 40:
        break
    else:
        print('Hibás adatbevitel vagy kezdő sorszám! Próbáld meg újra...')
while True:
    bef = int(input(f'Add meg a befejező sorszámot [1...{elemszam}]:'))
    if 1 <= bef <= 40 and bef > kezdo:
        break
    else:
        print('Hibás adatbevitel vagy befejező sorszám! Próbáld meg újra...')
for i in range(kezdo-1, bef):
    print(f"{i + 1}. elem: {lista[i]}")
#3 feladat
szorz = lista[-1] * lista[0]
osszeg = 0
for i in range(kezdo-1, bef):
    osszeg += lista [i]
print(f'A lista {kezdo}. és {bef}. közötti elemeinek összege: {osszeg}')
print(f'A lista első és utolsó elemének szorzata: {lista[0]} * {lista[-1]} = {szorz}')
if osszeg > szorz:
    print(f'A lista {kezdo}. és {bef}. közötti elemeinek összege a nagyobb.')
elif osszeg < szorz:
    print('A lista első és utolsó elemének szorzata a nagyobb.')
else:
    print(f'A lista {kezdo}. és {bef}. közötti elemeinek összege és a lista első és utolsó elemének szorzata egyenlő.')
#4 feladat
maxert = lista[0]
minert = lista[0]
for i in range(len(lista)):
    if lista[i] > maxert:
        maxert = lista[i]
        maxind = i
    elif lista[i] < minert:
        minert = lista[i]
        minind = i
print(f'A listában található legkisebb szám: {minert}')
print(f'A listában található legnagyobb szám: {maxert}')
if kezdo <= minind <= bef:
    print(f'A legkisebb elem megtalálható meg a(z) {kezdo}. és a(z) {bef}. sorszámú elemek között.')
else:
    print(f'A legkisebb elem nem található meg a(z) {kezdo}. és a(z) {bef}. sorszámú elemek között.')
if kezdo <= maxind <= bef:
    print(f'A legnagyobb elem megtalálható meg a(z) {kezdo}. és a(z) {bef}. sorszámú elemek között.')
else:
    print(f'A legnagyobb elem nem található meg a(z) {kezdo}. és a(z) {bef}. sorszámú elemek között.')
#5 feladat
kozkis = 0
eloford = 0
for i in range(kezdo-1, bef):
    if lista[i] < kozkis:
        kozkis = lista[i]
for i in lista:
    if kozkis == i:
        eloford +=1
print(f'A lista {kezdo}. és {bef}. elemei között található legkisebb szám: {kozkis}')
print(f'Előfordulások száma a teljes listában: {eloford} db')
#6 feladat
negativ = 0
for i in range(len(lista)):
    if lista[i] <= negativ:
        negativ = lista[i]
        negativhely = i
if negativ != 0:
    print(f'A listában található legnagyobb negatívszám: {negativ}, helye: {negativhely}. pozíció')
else:
    print('A listában nincs negatív szám.')