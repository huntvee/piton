file = open("2024_2_5/input2.txt")
sorok = file.readlines()
file.close()

szamok = []
for i in range(1, len(sorok)):
    szamok.append(int(sorok[i].strip()))
print(szamok)