import numpy as np


def knapsack(weight, prices, capacity, index=0):
    if capacity == 0 or index == len(weight):
        return 0

    left = 0

    if capacity >= weight[index]:
        left = prices[index] + knapsack(weight, prices, capacity - weight[index], index + 1)

    right = knapsack(weight, prices, capacity, index + 1)

    return max(left, right)


p = [7, 8, 6]
w = [10, 15, 5]

print(knapsack(w, p, 20))


def knapsackDP(weight, prices, capacity, memory, index=0):
    if capacity == 0 or index == len(weight):
        return 0

    if memory.get((capacity, index)):
        return memory.get((capacity, index))

    left = 0

    if capacity >= weight[index]:
        left = prices[index] + knapsackDP(weight, prices, capacity - weight[index], memory, index + 1)

    right = knapsackDP(weight, prices, capacity, memory, index + 1)
    res = max(left, right)

    memory[(capacity, index)] = res

    return res


po = np.random.randint(5, 20, 100)
wt = np.random.randint(3, 20, 100)

print(knapsackDP(wt, po, 200, {}))
