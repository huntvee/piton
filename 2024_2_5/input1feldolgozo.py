file = open("2024_2_5/input1.txt")
sorok = file.readlines()
file.close()
print(sorok)

szamok = []
for i in range(len(sorok)):
    """
    szam_str=sorok[i].strip()
    szam=int(szam_str)
    szamok.append(szam)
    """
    szamok.append(int(sorok[i].strip()))
print(szamok)
osszeg = 0
for i in range(len(szamok)):
    osszeg += szamok[i]
print(osszeg)