from collections import deque, OrderedDict, Counter, ChainMap


d = deque([1, 2, 3])
d.insert(-1, 1)
print(d)

od = OrderedDict(a=3, b=5, c=7)
od['d'] = 4
od['f'] = 6
od['e'] = 8
print(od)


s = 'sdfaksdfjoeiofjsiodfjie'
counter = Counter()
for c in s:
    counter[c] += 1
print(counter)

a = dict(a=1, b=2, c=3)
b = dict(d=4, e=5, g=6, h=7)
cm = ChainMap(a, b)
print(cm)
print(cm.maps)
a['a'] = 5
print(cm['a'])



