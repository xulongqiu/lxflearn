#!/usr/bin/python3.5

L = [x * x for x in range(1, 11)]
print(r"[x * x for x in range(1, 11)]")
print(L)

L = [x * x for x in range(1, 11) if x % 2 == 0]
print(r"[x * x for x in range(1, 11) if x % 2 == 0]")
print(L)

L = [m + n for m in 'ABC' for n in 'XYZ']
print(r"[m + n for m in 'ABC' for n in 'XYZ']")
print(L)

import os 

L = [d for d in os.listdir('.')]
print(r"[d for d in os.listdir('.')]")
print(L)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print(d)
for k,v in d.items():
    print(k, '=', v)

L = [k + '=' + v for k,v in d.items()]
print(r"[k + '=' + v for k,v in d.items()]")
print(L)

L = ['Hello', 'World', 'IBM', 'Apple']
l = [s.lower() for s in L]
print(r"[s.lower() for s in ['Hello', 'World', 'IBM', 'Apple']")
print(l)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(r"[s.lower() for s in L1 if isinstance(s, str)]")
print(L2)
