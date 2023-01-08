def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fib()
[next(f) for _ in range(10)]
