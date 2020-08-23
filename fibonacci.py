def fib(n):
    '''
    Return n-th Fibonacci number
    :param n: index of a Fibonacci number
    :return: number with index n from the Fibonacci sequence
    '''
    fib_l = list()
    fib_l.append(0)
    fib_l.append(1)
    for i in range(2, n+1):
        fib_l.append(fib_l[i-1] + fib_l[i-2])
    return fib_l[n]


def fib_digit(n):
    '''
    Return last digit of n-th Fibonacci number
    :param n: index of Fibonacci number
    :return: Last digit of a Fibonacci number with index n
    '''
    fib_d = list()
    fib_d.append(0)
    fib_d.append(1)
    for i in range(2, n + 1):
        fib_d.append((fib_d[i-2] + fib_d[i-1]) % 10)
    return fib_d[n]


def main():
    n = int(input())
    # print(fib(n))
    print(fib_digit(n))


if __name__ == "__main__":
    main()
