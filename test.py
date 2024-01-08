list =[1,24,653,24]

def osszeg(n):
    sum = 0
    for i in n:
        sum += i
    return(sum)
print(osszeg(list))