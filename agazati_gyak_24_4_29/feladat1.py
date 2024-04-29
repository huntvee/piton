import random
while True:
    szam = int(input('Add meg a lista méretét [10...20]: '))
    if 10 <= szam<= 20:
        break
    print('Hibás adatbevitel! Próbáld újra!')
elemek = []
osszeg = 0
for i in range(szam):
    elemek.append(random.randint(1, 5))
    osszeg += elemek[i]
print (f'A lista tartalma: {elemek}')
print (f'A listában lévő elemek összege: {osszeg}')
maxert = elemek[i]
maxindex = 0
for i in range(1, len(elemek)):
    if elemek[i] > maxert:
        maxert = elemek[i]
        maxindex = i+1
print (f'A legnagyobb elem: {maxert}, helye: {maxindex}. pozíció')