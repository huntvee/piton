'''
s = input('adj meg egy szamot ')
if int(s)%2==0:
    print('a szam kettovel oszthato')

'''
str = 'ez egy mondat. ez meg egy mondat.'

'''

if 'a' in string:
    print('az A betu benne van a szovegben')
for i in range(len(string)):
    if string[i] == 'a':
        hely = i

print(hely+1)

'''
mondatok = 0
for i in range(len(str)):
    if str[i] == '.' or str[i] == '!' or str[i]== '?':
        mondatok = mondatok+1
print (f'{mondatok} mondat van')