def fib_list(n):
    result  = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
        return result
print(fib_list(10))