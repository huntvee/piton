l = ["Geza", "Danika"]
f = open("24_5_13/output.txt", "w", encoding="utf-8")
for i in range(len(l)):
    f.write(f"{i+1}.név {l[i]}\n")
f.close()