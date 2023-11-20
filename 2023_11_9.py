def fejlec(cim):
    szelesseg = 30
    csillagok = '*'*szelesseg
    kozepso_csillag = "*"*int(((szelesseg-len(cim))/2)-1)
    print(csillagok)
    if len(cim)%2==1:
        print(kozepso_csillag+' '+cim+' '+kozepso_csillag+'*')
    else:
        print(kozepso_csillag+' '+cim+' '+kozepso_csillag)
    print(csillagok)

program_neve ='Programcime'
fejlec(program_neve)

#teszt=''
#for i in range(2,20):
#    teszt+='c'
#    fejlec(teszt)
#x=11_123_321
#print(x+1)

#8as számrendszer
print(0o123)
#16os szamrendszer
print(0xABBA)
#2es szamrendszer
print(0b11000000)

x=int('345', 8) #tetszoleges szamrendszer
print(x)

x=oct(321) #valtas 8asba
print(x)

x=hex(40096) #valtas 16osba
print(x)

x=bin(192) #valtas 2esbe
print(x)

print(1/100000000) #1e-8

str = 'Anya azt mondta hogy: "Érj vissza idoben!"'
print (str)

x= 6/4 
y = 6//4
z = 6%4 

print (x,y,z)