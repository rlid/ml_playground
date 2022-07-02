import time
import timeit


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_tr(n, a, b):
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        return fib_tr(n - 1, b, a + b)


t = time.time()
print(fib(35))
print(time.time() - t)
t = time.time()
print(fib_tr(35, 1, 1))
print(time.time() - t)
