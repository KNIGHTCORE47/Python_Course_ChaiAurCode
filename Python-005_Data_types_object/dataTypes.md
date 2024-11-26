# Data Types [Object Types]: 

Example:

- Number: 1234, 3.14, 3+4j, 0b1010, Decimal(), Fraction()

- String: 'Hello', "Hello", "Bob's world", b'a\x01c', u'sp\u00e9cial'

- List: [], ['Hello', 'World'], [1, 2, "3"], ['foo', 'bar', ['baz', 'qux']], list(range(10))

- Tuple: (), (1, 2, 3), (1, 2, "3"), ('foo', 'bar', ('baz', 'qux')), tuple(range(10)), namedtuple('Point', ['x', 'y'])

- Boolean: True, False

- Mapping(Dictionary): {}, {'one': 1, 'two': 2, 'three': 3}, dict(one=1, two=2, three=3)

- Set: {}, {1, 2, 3}, set([1, 2, 3, 59, 1, 8]), set('Mississippi')

- File: open(file, mode='r'), open(file, mode='w'), open(file, mode='a'), open('test.txt', 'w'), open(r'c:\test.txt', 'wb')

- Buffer: Bytes, bytearray, memoryview

- None: None

- Function: def func(): pass, lambda x: x*2

- Moudule: import module, import module as m, from module import func, from module import *

- Class: class Person: pass, class Person: def __init__(self, name): self.name = name

- Advance: Generator, Iterator, Decorator, Metaprogramming

NOTE - Python is a dynamically typed language. Helping method: dir()