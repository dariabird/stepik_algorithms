from functools import lru_cache
from matplotlib import pyplot as plt
import time


def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


old_fib1 = fib1


cache = {}
def fib2(n):
    assert n >= 0
    if n not in cache:
        cache[n] = n if n <= 1 else fib2(n - 1) + fib2(n - 2)
    return cache[n]


def memo(f):
    cache = {}

    def inner(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return inner


def fib3(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


def timed(f, *args, n_iter=100):
    acc = float('inf')
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1-t0)
    return acc


def compare(fs, args):
    for f in fs:
        plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    # fib1 = memo(old_fib1)
    # fib1 = lru_cache(maxsize=None)(old_fib1)
    # print(fib1(8000)) # max depth of recursion exceeded
    # print(fib3(8000))
    # print(timed(fib3, 800))
    compare([old_fib1, fib3], list(range(20)))

