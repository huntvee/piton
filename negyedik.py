list = [12,325,235,6801,135,5646]
legnagyobb = list[0]
index = 0
for i in range(len(list)):
    if list[i] > legnagyobb:
        legnagyobb = list[i]
        index = i
print (f'A legnagyobb szám {legnagyobb} és ez a listában a {index+1}. elem.')

string = 'Erik'
if 'a' in string:
    print ('megvan')
else:
    print ('nuh uh')

for i in range(len(string)):
    if 'a' not in string[i]:
        print ('nuh uh')
        break
    elif string[i] == 'a':
        print (f'megvan, {i+1}')
        break
