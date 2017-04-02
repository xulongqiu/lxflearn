#!/usr/bin/python3.5

# list, tuple, dict, set, srt is iterable, but is not iterator
# 生成器 和 带有yield 的generator is iterable and iterator

from collections import Iterable

print('Iterable ****')
print(r"isinstance([], Iterable)", isinstance([], Iterable))
print(r"isinstance({}, Iterable)", isinstance({}, Iterable))
print(r"isinstance('abc', Iterable)", isinstance('abc', Iterable))
print(r"isinstance((x for x in range(10)), Iterable)", isinstance((x for x in range(10)), Iterable))
print(r"isinstance(123, Iterable)", isinstance(123, Iterable))


from collections import Iterator
print('\nIterator ****')
print(r"isinstance((x for x in range(10)), Iterator)", isinstance((x for x in range(10)), Iterator))
print(r"isinstance([], Iterator)", isinstance([], Iterator))
print(r"isinstance({}, Iterator)", isinstance({}, Iterator))
print(r"isinstance('abc', Iterator)", isinstance('abc', Iterator))

print('\nIterable to Iterator ***')
print(r"isinstance(iter({}), Iterator)", isinstance(iter({}), Iterator))
print(r"isinstance(iter('abc'), Iterator)", isinstance(iter('abc'), Iterator))


