import math as m
def f(x:int, y:int) ->int:
    '''
        f(x,y)=3x+2y
    '''
    return 3*x+2*y
print(f(2,3))
print(f(3,2))
f(y=8, x=7)

def ki(x:any)->None:
    print(x)
x=print("szia")
ki(x)

if print("valami")==None:
    print("noneal tert vissza")

x=ki("géza")
if x==None:
    print("nem volt visszateresi ertek")
def masodfoku(a:float,b:float,c:float):
    if a==0:
        return
    d = b**2-4*a*c
    if d<0:
        return
    if d==0:
        x1=( -b )/(2*a)
    x1=( -b+m.sqrt(d) )/(2*a)
    x2=( -b-m.sqrt(d) )/(2*a)
    return x1,x2
x = masodfoku(1,3,1)
if x == None:
    print("nincs zerushely")
if type(x)==type(tuple()):
    print("ket zerushely van")