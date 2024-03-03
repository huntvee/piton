print()

"""
Egy Skodákat forgalmazó vállalatnak 5 telephelye van az országban. Az elmúlt
évben havonta eladott Octavia RS modellek darabszámát egy fájlban tartja nyilván.
"""
"""
1. feladat:
Olvasd be a fájl tartalmát egy megfelelő adatszerkezetbe! Ügyelj arra, hogy
a numerikus értékek számként legyenek tárolva.
"""
auto = []
f = open("korep/tz.txt", "r", encoding="UTF-8")
for sor in f:
    auto.append(sor.replace("\n", "").strip().split())
i = 0
while i <len(auto):
    j = 1
    while j < len(auto[i]):
        auto[i][j] = int(auto[i][j])
        j += 1
    i += 1
"""
2. feladat:
A példában látható módon írjuk ki az adatokat!
PÉLDA:
Város: Budapest
Január: 0 db
Február: 0 db
Március: 3 db
...

Város: Szeged
Január: 0 db
Február: 0 db
...
"""
hónapok = ("Január", "Február", "Március", "Április", "Május", "Június", "Július", "Augusztus", "Szeptember", "Október", "November", "December")
i = 0
while i < len(auto):
    print(f"\nVáros: {auto[i][0]}")
    j = 1
    while j < len(auto[i]):
        print(f"{hónapok[j - 1]}: {auto[i][j]} db")
        j += 1
    i += 1
"""
3. feladat:
A példában látható módon írjuk ki a képernyőre, hogy az egyes városokban
hány olyan hónap volt, amikor egy autót sem adtak el!
PÉLDA:
Eladásmentes hónapok városonként:
Budapest: 5 hónap
Szeged: 6 hónap
...
Kaposvár: 4 hónap
Összesen: 25 hónap
"""
osszeg = 0
i = 0
print(f"\nEladásmentes hónapok városonként:")
while i < len(auto):
    db = 0
    j = 1
    while j <len(auto[i]):
        if auto[i][j] == 0:
            db += 1
        j += 1
    print(f"{auto[i][0]}: {db}  hónap")
    i += 1
    osszeg += db
print(f"Összesen: {osszeg} hónap")
"""
4. feladat:
A példában látható módon írjuk ki a képernyőre, hogy az elmúlt évben melyik
hónapban adták el a legtöbb autót a kereskedés összes telephelyén!
PÉLDA:
Havonta eladott Octavia RS autók száma:
Január: 2 db
Február: 3 db
...
December: 12 db
Összesen: 98 db
Legsikeresebb hónap: augusztus (27 db)
"""
teljesDb= 0
i = 0
haviEladások = []
print(f"\nHavonta eladott Octavia RS autók száma:")
while i < len(hónapok):
    j = 0
    összeg = 0
    while j < len(auto):
        összeg += auto[j][i + 1]
        j += 1
    print(f"{hónapok[i]}: {összeg} db")
    teljesDb += összeg
    haviEladások.append(összeg)
    i += 1
print(f"Összesen: {teljesDb} db")
maxÉrték = haviEladások[0]
maxHely = 0
i = 0
while i < len(haviEladások):
    if haviEladások[i] > maxÉrték:
        maxÉrték = haviEladások[i]
        maxHely = i
    i += 1
print(f"Legsikeresebb hónap: {hónapok[maxHely].lower()} ({maxÉrték} db)")
"""
5. feladat (HF):
Igaz-e az az állítás, hogy minden telephelyen volt legalább 3 db olyan hónap,
amikor legalább 3 autót eladtak?
PÉLDA:
Feltételnek megfelelő eladások városonként:
Budapest: 5 hónap
Szeged: 4 hónap
...
Kaposvár: 5 hónap
Igaz az állítás.
"""

print()