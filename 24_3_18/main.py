import sys
if len(sys.argv) < 2:
    print("Nem adtal meg filenevet")
    print(f"Helyes: py {sys.argv[0]} filename")
else:
    filename = sys.argv[1]
    print(filename)
    file = open(filename)
    sorok = file.readlines()
    file.close()
    for i in range(len(sorok)):
        print(sorok[i].strip())
