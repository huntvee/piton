# 1. Feladat: Olvassuk be a filet soronkent, es listaba taroljuk el. A szoveg a fajlbol nem kell. (Pl.: [ [1,2,3,4],[1,2,3,4],[1,2,3,4] ])
# 2. Feladat: Szamoljuk meg hogy mennyi az osszes szam osszege, es hogy mennyi a sorok osszege. (Pl.: 'A fajl osszege: 123
#                                                                                                      Az 1. sor osszege: 123
#                                                                                                      ...
#                                                                                                      A 4. sor osszege: 123')
# 3. Feladat: Kerjunk be a felhasznalotol egy szamot, es nezzuk meg, hogy benne van e listaban, es ha igen, irjuk ki hogy benne van,
#             es hogy hanyszor van benne. (Pl.: "A keresett szam: 3. A szambol 5 darab van a listaban.")
# 4. Feladat: Irjuk ki, hany paros es paratlan szam van. (Pl.: "Paros szamok: 13. Paratlan szamok: 8")
# 5. Feladat: Keressuk meg, hogy melyik a legnagyobb szam, es hol van a listaban. (Pl.: "A legnagyobb szam: 15. Helye: 2. sor, 5. szam.")

lista = []
f = open("korep/input.txt", "r", encoding="UTF-8")
for sor in f:
    lista.append(sor.replace("\n", "").strip().split())

del lista[0]
del lista[-1]

i = 0
while i < len(lista):
    j = 0
    while j < len(lista[i]):
        lista[i][j] = int(lista[i][j])
        j += 1
    i += 1
f.close()

print(lista)

osszeg = 0
sorosszeg = 0
i = 0
while i < len(lista):
    j = 0
    while j < len(lista[i]):
        osszeg += lista[i][j]
        sorosszeg += lista[i][j]
        j += 1
    i +=1
    print(f'Az {i}. sor osszege: {sorosszeg}')
    sorosszeg = 0
print (f'A fajl osszege: {osszeg}')

szam = int(input('adj szamot '))
darab = 0
van = None
i = 0
while i < len(lista):
    j = 0
    while j < len(lista[i]):
        if szam == lista[i][j]:
            darab += 1
            van = True
        j +=1
    i += 1
if van:
    print(f'A keresett szam: {szam}. A listaban ennyi darab van: {darab}')
else:
    print('nincs benne')

paros = 0
paratlan = 0
i = 0
while i < len(lista):
    j = 0
    while j < len(lista[i]):
        if lista[i][j]%2==0:
            paros +=1
        else:
            paratlan +=1
        j +=1
    i += 1
print (f'Paros szamok: {paros}. Paratlan szamok {paratlan}.')

maxertek = 0
maxhely = 0
maxsor = 0
i = 0
while i < len(lista):
    j = 0
    while j < len(lista[i]):
        if lista[i][j] >= maxertek:
            maxertek = lista[i][j]
            maxhely = j
            maxsor = i
        j +=1
    i += 1
print (f'A legnagyobb szam: {maxertek}. Helye: {maxsor+1}. sor, {maxhely+1}. szam.')