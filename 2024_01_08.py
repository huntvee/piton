osztaly1 = []
import random
ertek = None
while True:
    ertek = input('Add meg az értéket! 0-100: Írd be hogy "vége" hogy befejezd a megadást. ')
    if ertek == 'vége':
        break
    elif 0 < int(ertek) < 100:
        osztaly1.append((int(ertek)))
    else:
        print('Hibás számbevitel.')
#2 feladat
minert = None
maxert = None
while True:
    minert = int(input(f'Add meg a kezdő sorszámot [1...100]:'))
    if 0 <= minert <= 100:
        break
    else:
        print('Hibás adatbevitel vagy kezdő sorszám! Próbáld meg újra...')
while True:
    maxert = int(input(f'Add meg a befejező sorszámot [1...100]:'))
    if 0 <= maxert <= 100 and maxert > minert:
        break
    else:
        print('Hibás adatbevitel vagy befejező sorszám! Próbáld meg újra...')
print("A megadott értékek kozott lévo számok: ", end="")
for i in osztaly1:
    if minert <= i <= maxert:
        print(i, end=" ")
#3 feladat
osszeg = 0
for i in osztaly1:
    osszeg += i
atlag1 = osszeg/len(osztaly1)
print(f'Az osztály átlaga:{atlag1}')
#4 feladat
osztaly2 = []
for i in range(len(osztaly1)):
    osztaly2.append(random.randint(0,100))
osszeg2 = 0
for i in osztaly2:
    osszeg2 += i
atlag2 = osszeg2/len(osztaly2)
if atlag1 > atlag2:
    print(f'Az elso osztaly atlaga nagyobb, {atlag1-atlag2}-vel')
elif atlag2 > atlag1:
    print(f'Az második osztaly atlaga nagyobb, {atlag2-atlag1}-vel')
else:
    print('A két osztály átlaga egyenlo.')