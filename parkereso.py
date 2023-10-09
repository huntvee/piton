lista = [
    ['Béla', 'f', '18:00'],

    ['Judit', 'n', '18:01'],

    ['Zoli', 'f', '18:06'],
]
egysor = ''
for i in range(len(lista)):
    for j in range(len(lista[i])):
        egysor += lista[i][j] + ' '
print (egysor)
i = 0
while (not (lista[i][1] == "n")):
    i= i+1
print(lista[i][0])