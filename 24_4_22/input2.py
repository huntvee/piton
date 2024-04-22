import sys
import os
## Fájl beolvasás
def nincsfajl():
    print("Nem érkezett adat!")
    print("Usage: py filename.py filename.txt")
def beolvas(filename):
    szamok = []
    nevek = []
    filename = sys.argv[1]
    file = open(filename, encoding="utf-8")
    rows = file.readlines()
    file.close()
    for i in range(1, len(rows)):
        rows[i] = rows[i].strip()
        szamok.append(rows[i].split(','))
    for i in range(len(szamok)):
        nevek.append(szamok[i][-1])
        del szamok[i][-1]
        for x in range(len(szamok[i])):
            szamok[i][x] = int(szamok[i][x])
    return szamok, nevek
    
if len(sys.argv) <= 1:
    nincsfajl()
elif os.path.exists(sys.argv[1]):
    szamok = beolvas(sys.argv[1])[0]
    nevek = beolvas(sys.argv[1])[1]
    print(szamok, nevek)