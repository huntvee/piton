print (float(5>>1))
fajlnev = 'input.txt'
f = open(fajlnev, "r")
sorok=f.readlines()
f.close()
for i in range(len(sorok)):
    sorok[i]=sorok[i].strip()
print(sorok[0])
sum = int(sorok[1])+int(sorok[2])
print(sum)
print(sorok)
l=[]
for i in range(10):
    l.append(i**2)
print(l)
l = [i**2 for i in range(10)]
print(l)