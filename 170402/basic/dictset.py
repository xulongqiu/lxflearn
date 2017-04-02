#!/usr/bin/python3.5


print('dict ****')

d = {}

d['Eric'] = 1
d['Alex'] = 2

print(d)

if 'Eric' in d:
    print('d[\'Eric\']=', d['Eric'])

print('d[\'Fly\']=', d.get('Fly'))

for key in d:
    print('d[%s]=' %key, d[key])

allclass = {}
class_1 = ['student1', 'student2', 'student3']
class_2 = ['student1', 'student2', 'student3']
class_3 = ['student1', 'student2', 'student3']
allclass['1'] = class_1
allclass['2'] = class_2
allclass['3'] = class_3
print(allclass)

print('set ****')
s =set(list(range(5)))
print(s)
s.add(5)
s.add(1)
print(s)

s.remove(1)
print(s)

a = set([1,2,3])
b = set([2, 3, 5])
print('a=%s, b=%s' %(a, b))
print('a & b =', a & b)
print('a | b = ', a | b)
