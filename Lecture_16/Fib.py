def fib(n):

    if n < 2:
        return n

    first = fib(n - 1)
    second = fib(n - 2)

    return first + second


print(fib(5))
