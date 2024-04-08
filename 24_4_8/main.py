import sys
import os
## Adatok kivétele a py argument után
'''
print("Hello ", end="")
print(sys.argv[1])
'''

## Fájl beolvasás
if len(sys.argv) <= 1:
    print("Nem érkezett adat!")
    print("Usage: py filename.py filename.txt")
elif os.path.exists(sys.argv[1]):
    filename = sys.argv[1]
    file = open(filename, encoding="utf-8")
    rows = file.readlines()
    file.close
    lista = []
    if sys.argv[1] == "input1.txt":
        for i in range(len(rows)):
            rows[i] = rows[i].strip()
            print(f"{rows[i]}")
    elif sys.argv[1] == "input2.txt":
        for i in range(1, len(rows)):
            rows[i] = rows[i].strip()
            print(f"{rows[i]}")
    elif sys.argv[1] == "input3.txt":
        for i in range(1, len(rows)-1):
            rows[i] = rows[i].strip()
            print(f"{rows[i]}")
    elif sys.argv[1] == "input4.txt":
        for i in range(1, len(rows)):
            rows[i] = rows[i].strip().split()
            lista.append(rows[i])
        print(lista)
else:
    print("Nem létezik ilyen fájl.")