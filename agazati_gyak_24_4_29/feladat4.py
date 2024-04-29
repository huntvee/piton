import random
while True:
    szam = int(input('Add meg a lista méretét [5...25]: '))
    if 5 <= szam<= 25:
        break
    print('Hibás adatbevitel! Próbáld újra!')
számok = []
osszeg = 0
count = 0
negativelemek = 0
for i in range(szam):
    számok.append(random.randint(-10, 10))
    osszeg += számok[i]
    if számok[i] == 0:
        count +=1
    if számok[i] < 0:
        negativelemek += 1
print (f'A lista tartalma: {számok}')
print (f'A listában lévő elemek összege: {osszeg}')
print (f'A listában lévő 0 elemek száma: {count}')
print (f'A listában lévő negatív elemek száma: {negativelemek}')
if count > negativelemek:
    print('Az állítás igaz!')
elif count < negativelemek:
    print('Nem igaz az állítás!')