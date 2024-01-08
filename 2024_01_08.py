osztaly1 = []
ertek = None
while True:
    ertek = input('Add meg az értéket! 0-100: Írd be hogy "vége" hogy befejezd a megadást. ')
    if ertek == 'vége':
        break
    elif 0 < int(ertek) < 100:
        osztaly1.append((int(ertek)))
    else:
        print('Hibás számbevitel.')