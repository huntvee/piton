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
        nevek.append(szamok[i][0])
        del szamok[i][0]
        for x in range(len(szamok[i])):
            szamok[i][x] = int(szamok[i][x])
    return szamok, nevek
def maxkedd(szamok, nevek):
    maxert = 0
    maxnev = None
    for i in range(len(szamok)):
        if szamok[i][1] > maxert:
            maxert = szamok[i][1]
            maxnev = nevek[i]
    return maxert, maxnev
def szerda(szamok, nevek):
    maxert = 0
    maxnev = 0
    atlag = 0
    for i in range(len(szamok)):
        atlag = atlag+szamok[i][2]
    atlag = atlag/len(szamok)
    for i in range(len(szamok)):
        if szamok[i][2] > atlag:
            maxert = szamok[i][2]
            maxnev = nevek[i]
    return maxert, maxnev
def ossz(szamok):
    s = 0   
    for i in range(len(szamok)):
        for x in range(len(szamok[i])):
            s = s+szamok[i][x]
    return s
def yen(szamok):
    atlag = 0
    for i in range(len(szamok[3])):
        atlag = atlag+szamok[3][i]
    atlag = atlag/len(szamok[3])
    return atlag
    
if len(sys.argv) <= 1:
    nincsfajl()
elif os.path.exists(sys.argv[1]):
    szamok = beolvas(sys.argv[1])[0]
    nevek = beolvas(sys.argv[1])[1]
    print(f'Kedden a legtobbet {maxkedd(szamok, nevek)[1]} készitette')
    print(f"Szerdan az atlag felett {szerda(szamok, nevek)[1]} volt")
    print(f"Yennifer átlaga: {yen(szamok)}")