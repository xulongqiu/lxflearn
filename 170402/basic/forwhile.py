#!/usr/bin/python3.5

names = ['Eric', 'Alex', 'Leo', 'Fly']
for name in names:
    print(name)

sum = 0
for x in range(101):
    sum += x
print('1+..+100=', sum)

print('break ****')
sum = 0
n = 1
while True:
    if n > 100:
        break

    sum += n
    #do not suport n++ 
    n += 1

print('1+..+100=', sum)


print('continue ****')
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)


