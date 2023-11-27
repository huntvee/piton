import random
import calendar
hetek = 0
#1 feladat
while hetek > 5 or 1 > hetek:
    hetek = int(input('Add meg a hetek számát [1...5]: '))
    if hetek > 5 or 1 > hetek:
        print('Hibás adatbevitel! Próbáld meg újra...')
#2 feladat
tamadasok = []
for i in range(hetek):
    tamadasok.append([])
for i in range(len(tamadasok)):
    for n in range(0,7):
        tamadasok[i].append(random.randint(3,9))
#3 feladat
    print(f'{i+1}. Hét: ', end='')
    c = 0
    for x in range(len(tamadasok[i])):
        print(tamadasok[i][x], end=' ')
        if x%6 == 0 and x != 0:
            print()
#4 feladat
osszes = 0
for i in range(hetek):
    for n in tamadasok[i]:
        osszes+=n
print (f'Összes támadás száma: {osszes} db')
#5 feladat
megfelel = 0
for i in range(hetek):
    for n in tamadasok[i]:
        if n < 8 and n > 5:
            megfelel+=1
print(f'Feltételnek megfelelő napok száma: {megfelel} db')
#6 feladat
legtobb = 0
legtobbhet = 0
legtobbnap = 0
for i in range(hetek):
    for n in range(len(tamadasok[i])):
        if tamadasok[i][n] >= legtobb:
            legtobb = tamadasok[i][n]
            legtobbhet = i
            legtobbnap = n
#1 megoldás
def nap(n):
    if n+1 == 1:
        return ('Hétfő')
    elif n+1 == 2:
        return ('Kedd')
    elif n+1 == 3:
        return ('Szerda')
    elif n+1 == 4:
        return ('Csutortok')
    elif n+1 == 5:
        return ('Péntek')
    elif n+1 == 6:
        return('Szombat')
    elif n+1 == 7:
        return('Vasárnap')
print (f'Egy napon megtörtént legtöbb támadás száma: {legtobb} db')
print (f'Helye: {legtobbhet+1}. hét, {nap(legtobbnap)}')
#2 megoldás
'''
print (f'Egy napon megtörtént legtöbb támadás száma: {legtobb} db')
print (f'Helye: {legtobbhet+1}. hét, {calendar.day_name[legtobbnap]}')
'''