d = {'name':'phb', 'age':12}

print(d.get('abc') is None)

def returnabc(a, b, c):
    return a, b, c

i, j, k = returnabc(1, 2, 3)
print(i, j, k)