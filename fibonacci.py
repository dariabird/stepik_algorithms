def fib(n):
    '''
    Return n-th Fibonacci number
    :param n: index of a Fibonacci number
    :return: number with index n from the Fibonacci sequence
    '''
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


def fib_digit(n):
    '''
    Return last digit of n-th Fibonacci number
    :param n: index of Fibonacci number
    :return: Last digit of a Fibonacci number with index n
    '''
    f0, f1 = 0, 1
    for i in range(2, n + 1):
        f0, f1 = f1 % 10, (f0 + f1) % 10
    return f1


def main():
    n = int(input())
    # print(fib(n))
    print(fib_digit(n))


if __name__ == "__main__":
    main()
