#!/usr/bin/python3.5


#string of python
print('STRING OF PYTHON *******')
print('包含中文的str')

print('A=', ord('A'))
print('中=', ord('中'))
print('66=', chr(66))
print('25991=', chr(25991))
print('\u4e2d\u6587')

#bytes
x = b'ABC'
print(x)

#Unicode
print('\'ABC\'.encode(\'ascii\')=', 'ABC'.encode('ascii'))
print(r"'中文'.encode('utf-8')=", '中文'.encode('utf-8'))
print(r"b'ABC'.decode('ascii')=", b'ABC'.decode('ascii'))
print(r"b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')=", b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(r"len('ABC')=", len('ABC'))
print(r"len('中文')=", len('中文'))
print(r"len(b'ABC')=", len(b'ABC'))
print(r"len(b'\xe4\xb8\xad\xe6\x96\x87')=", len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(r"len('中文'.encode('utf-8'))=", len('中文'.encode('utf-8')))

#format string
print('STRING FORMAT *******')
print('Hi, %s, you have $%d.' %('Eric', 521))

#all can be formated by %s
print('Age:%s, Gener:%s' %(28, True))

#print %
print('growth rage:%d%%' %89)

