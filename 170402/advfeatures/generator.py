#!/usr/bin/python3.5

g = (x * x for x in range(10))
print(r"g = (x * x for x in range(10))")
print('>>> g', g)

for n in g:
    print(n)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3

o = odd()
next(o)
next(o)
next(o)
#next(o) #StopIteration

#function Fibonacci
#1,1,2,3,5,8,13,21,34 ...

def fib_f(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'

print('fib_f(6)=')
fib_f(6)

def fib_g(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'none'

print('fib_g(6)=')
print(fib_g(6))

g = fib_g(6)

while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


#yanghui triangels
def triangles():
    L1 = [1]
    while True:
        yield L1
        L2 = [1]
        [L2.append(L1[i-1] + L1[i]) for i in range(len(L1)) if i > 0]
        #for i in range(len(L1)):
        #    if i > 0:
        #        L2.append(L1[i-1] + L1[i])
        L2.append(1)
        L1 = L2

n = 0
for t in triangles():
    print(t)
    if n >= 10:
        break
    n += 1


