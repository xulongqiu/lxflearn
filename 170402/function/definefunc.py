#!/usr/bin/python3.5

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print('my_abs(-23)=', my_abs(-23))

print('nop function ****')
def nop():
    pass

print('my_abs with paras check ***')
def my_abs_with_paras_check(x):
    if not isinstance(x,(int, float)):
        raise TypeError('Bad operand type')
    if x >= 0:
        return x
    else:
        return -x

#my_abs_with_paras_check('A')

print('return multi value ****')
def area_perimeter(x, y):
    if not isinstance(x, (int, float)):
        raise TypeError('Bad operand type')
    if not isinstance(y, (int, float)):
        raise TypeError('Bad operand type')
    return 2 * (x + y), x * y

print('rectangle[2, 5]=', area_perimeter(2, 5))
