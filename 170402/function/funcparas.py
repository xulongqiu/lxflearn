#!/usr/bin/python3.5

#default parameters
def power(x, n=2):
    s = 1
    while n > 0:
        s *= x
        n -=1
    return s

print('power(5)=%d, power(5, 2)=%d, power(5, 3)=%d' %(power(5), power(5,2), power(5,3)))

def enroll(name, gender, age = 6, city = 'Beijing'):
    print('%s:gender(%s), age(%d), city(%s)' %(name, gender, age, city))

print(r"enroll('Sarah', 'F')=", enroll('Sarah', 'F'))
print(r"enroll('Bob', 'M', 7)=", enroll('Bob', 'M', 7))
print(r"enroll('Adam', 'M', city = 'Tianjin')=", enroll('Adam', 'M', city = 'Tianjin'))

#Note, default parameters must be constant variable
def add_end(L=[]):
    L.append('END')
    return L

print('add_end([1, 2, 3])=', add_end([1, 2, 3]))
print(r"add_end(['x', 'y', 'x'])=", add_end(['x', 'y', 'y']))
print('add_end()=', add_end())
print('add_end()=', add_end())

def add_end_2(L = None):
    if L is None:
        L = []
    L.append('END')
    return L

print('add_end_2()=', add_end_2())
print('add_end_2()=', add_end_2())

#cnt of paras isn't constant

#calc(1, 2, 3) = 1 * 1 + 2 * 2 + 3 * 3
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum

print('calc(1, 2, 3)=', calc(1, 2, 3))
print('calc(1, 2)=', calc(1, 2))
nums = [1, 2, 3, 4]
print('calc(*nums)=', calc(*nums))


#keyword paras
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

print(r"person('Michel', 30)=", person('Michel', 30))
print(r"person('Alex', 35, city='Beijing')=", person('Alex', 35, city='Beijing'))
print(r"person('Frank', 26, city='Tianjin', job='Engineer')=", person('Frank', 26, city='Beijing', job='Engineer'))
extra = {'job':'Engineer'}
extra['city'] = 'Beijing'
print(r"person('Jhon', 23, **extra)=", person('Jhon', 23, **extra))

#named keyword paras
def person2(name, age, *, city, job):
    print(name, age, city, job)

print(r"person2('Jack', 23, city = 'Beijing', job='Engineer')=", person2('Jack', 23, city = 'Beijing', job='Engineer'))

print('parameters sequence: must paras, default paras, *args, **namedkw, **kw')


