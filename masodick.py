def kiir(str):
    print(str)
kiir(5)
kiir('szia')

def g_fv(x,y,z):
    return x*x+y+z/2
x = g_fv(5,3,4)
kiir(x)

def lista_osszeg(lista):
    sum = 0
    for i in range(len(lista)):
        sum+= lista[i]
    return sum
l1=[1,3,5,7]
l2=[7,2,9]
l3=[6,3,0,4]
print(lista_osszeg(l1))
print(lista_osszeg(l2))
print(lista_osszeg(l3))

def lista_atlag(lista):
    atlag = lista_osszeg(lista)
    return atlag/len(lista)
print (lista_atlag(l1))