#!/usr/bin/python3.5

###integer
print('INTEGER*******')
print(1, 100, -67, 0, 0xff00, 0xa5b4c3d2)

###float
print('\nFLOAT*******')
print(3.1415, -0.465, 1.23e9, 12.2e-2)


###string
print('\nSTRING*******')
#abc
print('adb')

#I'm OK！
print("I'm OK!")

#I'm "OK"
print('I\'m \"OK\"')

#use r'' print them as they are
print(r'I\'m \"OK\"')

#print multi ines use ''' '''
print('''line1
line2
line3''')

print(r'''line1
line2
line3''')

#boolean
print('\nBOOLEAN*******')
print('(3 > 2)=', 3 > 2)
print('(3 > 5)=', 3 > 5)

#and
print('(True and Ture)=', True and True)
print('(5 > 3 and 3 > 6)=', 5 > 3 and 3 > 5)

#or
print('(True or False)=', True or False)
print('(5 > 3 or 3 > 6)=', 5 > 3 or 3 > 6)

#not
print ('(not True)=', not True)
print ('(not 1 > 2)=', not 1 > 2)

#None 
print('\nNone*******')
print('(None)=', None)


#Variables 
print('\nVARIABLES*******')
a = 1
name = 'eric.xu'
answer = True

#python is dynamic language
var=1 #var is integer
print(var)
var='ABC' #var is string
print(var)

#But in C langunge
#int var = 1 // var is integer
#var = "ABC" //build error


#constant
print('\nCONSTAND*******')
PI = 3.141592653
print('PI=', PI)

#divison
print('\nDIVISION*******')
print('10//3=', 10//3)
print('10/3=', 10/3)
print('10%3=', 10%3)
