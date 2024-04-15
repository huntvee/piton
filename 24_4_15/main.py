import sys
print("Hello")
print(sys.argv)
l = [[1,2,3],
     [4,5,6],
     [7,8,9]]
def maxkivkedd (matrix):
    oszlop = 1
    maxert = matrix[0][oszlop]
    maxsor = 0
    for i in range (1,len(matrix)):
        if maxert < matrix[i][oszlop]:
            maxert = matrix[i][oszlop]
            maxsor = i
    return maxsor, maxert
def sorosszeg (lista):
    s = 0
    for i in range(len(lista)):
        s += lista[i]
    return s
sorosszeg(l[0])

def maxsorosszeg(m):
    maxertek = sorosszeg(m[0])
    maxindex = 0
    for i in range(1, len(m)):
        if maxertek < sorosszeg(m[i]):
            maxertek = sorosszeg(m[i])