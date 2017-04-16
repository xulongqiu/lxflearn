#!/usr/bin/python3.5

d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

print('d=', d)

for key in d:
    print('key=', key, 'value=', d[key])

for k, v in d.items():
    print('key=', k, 'value=', v)

for v in d.values():
    print('v=', v)

from collections import Iterable
print(r"isinstance('ABC', Iterable)=", isinstance('ABC', Iterable))
print(r"isinstance([1,2,3], Iterable)=", isinstance([1,2,3], Iterable))
print(r"isinstance(123, Iterable)=", isinstance(123, Iterable))

print(r"for i, v in enumerate(['A', 'B', 'C'])")
for i, v in enumerate(['A', 'B', 'C']):
    print(i, v)

print(r"for x, y in [(1,1), (2,4), (3,9)]")
for x, y in [(1,1), (2,4), (3,9)]:
    print(x, y)


