while True:
    szamstr=input('Adj meg egy egész számot! ')
    if szamstr.isdecimal():
        szam=int(szamstr)
        break
if szam > 3:
    print('a szam nagyobb mint 3')
elif szam < 3:
    print('a szam kisebb mint 3')