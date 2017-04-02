#!/usr/bin/python3.5

#list
print('LIST *******')
classmates = ['Eric', 'Alex', 'Jhon', 'Frank']
print('%d students:' %len(classmates), classmates)
print('classmates[0]=', classmates[0])
print('classmates[-1]=', classmates[-1])

classmates.append('Fly')
print('%d students:' %len(classmates), classmates)
classmates.insert(1, 'Adam')
print('%d students:' %len(classmates), classmates)
classmates.pop()
print('%d students:' %len(classmates), classmates)

#different type of data in list
L = ['iPhone', 'Huawei', 3, 4, True]
print(L)

#list in list
S = ['C', 'C++', ['PHP', 'Python']]
print('%d elements:' %len(S), S)

#tuple, its content is constant once define
print('\nTUPLE *******')
teachers = ('Michael', 'Bob', 'Tracy')
print('%d teachers:' %len(teachers), teachers)
print('teachers[-1]=', teachers[-1])
t = (1, 2)
print('t(1, 2)=', t)
t=()
print('t()=', t)
t = (1)
print('t(1)=', t)
t = (1,)
print('t(1,)=', t)

#list in tuple
t = (1, 2, ['x', 'Y'])
print(t)
t[2][0] = 'A'
t[2][1] = 'B'
t[2].append('C')
print(t)





