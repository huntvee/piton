filename="input.txt"
file=open(filename, "r")
file_lista=file.readlines()
file.close
name_list=[]
pancake_list=[]
for i in range(len(file_lista)):
    _lista_parts=file_lista[i].strip().split()
    name_list.append(_lista_parts[0])
    _l = []
    for j in range (1, len(_lista_parts)):
        _l.append(int(_lista_parts[j]))
    pancake_list.append(_l)
    print(_lista_parts[0])
print(name_list)
print(pancake_list)