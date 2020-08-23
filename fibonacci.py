def fib(n):
    fib_l = list()
    fib_l.append(0)
    fib_l.append(1)
    for i in range(2, n+1):
        fib_l.append(fib_l[i-1] + fib_l[i-2])
    return fib_l[n]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
