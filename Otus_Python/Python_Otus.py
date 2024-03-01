array=[2,5,6,9,12]
array.append(54,)
array.insert(0, 8)
array.pop() #Убрать элемент из списка, можно передать индекс
dict={'key' : 'value'}
dict['spam'] = 'egge'
dict.items()#получить значени dict
matrix = [
    [1, 4, 8],
    [9, 6, 3],
    [5,  76, 12]
]
a = 7
b = 9
if a > b:
    value = a + 2
else:
    value = b // 3
print(value)
print(matrix[1])
print(array, dict)

q = 0
w = 74
if q > 0 and w > 0:
    respons = 'true'
else:
    respons = 'falshe'
print('value :', respons)
result = []
values = {1, 4, 7, 9}
for value in values:
    result.append(value ** 2)
print(result)
for c in 'asdfgh':
    print(c, end=' ')
string = ''
strings = ['ass', 'tru', ' rew']
for s in strings:
    string += s
    print(string)
[val ** 2 for val in values]

line = ['spam', 'eggs', 'another line']
for lines in line[:]:
    if len(lines) > 7:
        line.insert(0, lines)
print(line)
for i in range(1, 5):
    print(i, end=' is ')
    if i % 2 == 0:
        print('even')
    else:
        print('odd')
def out_fun():
    def inner():
        return 'inner string'
    return inner()
print(out_fun())

def func():
    return 45, 'spam'
a, b = func()
print(a, b)

def den():
    yield 42,
print(den())

def fib(n):
    result = []
    a, b = 0, 1
    while a < n :
        result.append(a)
        a, b = b, a + b
    return result
print(fib(100))

def recur_fib(n):
    if n <=1:
        return n
    return recur_fib(n - 1) + recur_fib(n - 2)
print(recur_fib(10))
from functools import reduce
to_mul = range(1,8)
product = reduce(lambda x, y: x * y, to_mul)
print(product)
def decorator(func):
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args, **kwargs)
    return wrapper
@decorator
def count(a, b):
    return a + b

count(a=5, b=7)

from contextlib import contextmanager
@contextmanager
def managed_res(*args, **kwargs):
    print(*args, **kwargs)
    yield 42
    print('Closed')
with managed_res(1, 2, 3) as res:
    print(res, res + 100)
    print('Leaving')
print('left')

numbers = range(4)
result = list(map(lambda x: x**x, numbers))
print(numbers)
print(result)

a=16
b=0
if a > 0 and b > 0:
    print('true')
elif a > 0 and b == 0:
    print('b = 0')
else:
    print('falshe')

result = []
l = [1,  4, 6, 8, 11, 13, 16]
for item in l:
    result.append(item ** 2)
    print(result)


