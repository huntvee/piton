lista = []

filename="24_4_8/input4.txt"
file=open(filename, "r", encoding="UTF-8")

for sor in file:
    sor_elem = sor.strip().split()
    lista.append(sor_elem)
file.close()
print(lista)