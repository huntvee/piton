def osszegzes(l:list):
    """
    Osszegzes prog tetel
    return elemek osszege
    """
    s = 0
    for i in range(len(l)):
        s += l[i]
    return s
print(osszegzes([2,3,4]))
def megszamolas(l:list):
    c = 0
    for i in range(len(l)):
        c += 1
    return c
print(megszamolas([1,2,2,34,2,24]))
def maxert(l:list):
    mxert = 0
    mxindex = 0
    for i in range(len(l)):
        if l[i] > mxert:
            mxert = l[i]
            mxindex = i
    return mxert, mxindex
print(maxert([1,4,62,47,2334]))
def kereses(l:list, x):
    for i in range(len(l)):
        if l[i] == x:
            return i+1, x
print(kereses(l=[23,35,75,23,3], x=3))
def eldontes(l:list, x):
