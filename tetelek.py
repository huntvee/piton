def osszegzes_tetel(l:list, func)->int:
    szum = l[0]
    for i in range(1, len(l)):
        szum = func(szum, l[i])
    return szum

def osszead(num1,num2):
    return num1+num2

def szorzas(num1,num2):
    return num1*num2

print(osszegzes_tetel([1,2,3,4,5], lambda num1,num2:num1+num2))
print(osszegzes_tetel([1,2,3,4,5], lambda num1,num2:num1*num2))
osszeadas = lambda num1,num2:num1+num2
print(osszegzes_tetel([1,2,3,4,5], osszeadas))

def megszámlálás(l:list, condition)->int:
    count = 0
    for i in range(len(l)):
        if condition(l[i]) == 0:
            count += 1
    return count

def paros(num:int)->bool:
    return num%2==0
    
print(megszámlálás([1,2,3,4,5], lambda num: num%2==0))

def maxkivalasztas(l:list, condition)->tuple:
    maxind = 0
    maxert = l[0]
    for i in range(len(l)-1):
        if condition(l[i], maxert):
            maxind = i
            maxert = l[i]
    return maxind, maxert

def kisebb(num1,num2):
    return(num1< num2)

def nagyobb(num1,num2):
    return(num1> num2)

def keresés(l:list):
    for i in range(len(l)):
        if l[i] == 0:
            return True, i
    return False

def eldöntés(l:list)->bool:
    for i in range(len(l)):
        if l[i] == 0:
            return True
    return False

def kiválasztás(l:list)->int:
    for i in range(len(l)):
        if l[i] == 0:
            return l[i], i