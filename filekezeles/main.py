filename="input.txt"

file=open(filename, "r")
file_lista=file.readlines()
file.close()
lista=[]

for i in range(len(file_lista)):
    _lista=file_lista[i].strip()
    _lista_parts=_lista.split()
    _l=[]
    for j in range(len(_lista_parts)):
        _l.append(int(_lista_parts[j]))
    lista.append(_l)
print (lista)
while True:
    valasz = int(input("1. Számok összege \n 2. Számok soronkénti összege \n 3. Számok oszloponkénti összege \n 0. Kilépés \n"))
    if valasz == 1:
        osszeg = 0
        for i in range(len(lista)):
            for x in range(len(lista[i])):
                osszeg += lista[i][x]
        print (f'A számok osszege: {osszeg}')
    elif valasz == 2:
        for i in range(len(lista)):
            print(f'Az {i+1} sor osszege: {sum(lista[i])}')
    elif valasz == 3:
        oszlopok_szama = max(len(oszlop) for oszlop in lista)  
        oszlop_osszeg = [0] * oszlopok_szama  
        for oszlop in lista:
            for i, ertek in enumerate(oszlop):
                oszlop_osszeg[i] += ertek
        for i, oszl_ert in enumerate(oszlop_osszeg, 1):
            print(f"{i}. oszlop: {oszl_ert}")
    elif valasz == 0:
        break
    else:
        print('Hibás adatbevitel.')