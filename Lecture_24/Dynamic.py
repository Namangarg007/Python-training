def fibo(n):
    if n < 2:
        return n

    first = fibo(n - 1)
    second = fibo(n - 2)

    return first + second


def fiboDP(n, memory):
    if n < 2:
        return n

    if memory.get(n):
        return memory.get(n)

    first = fiboDP(n - 1, memory)
    second = fiboDP(n - 2, memory)

    memory[n] = first + second

    return first + second

print(fiboDP(50, {}))