def is_Sorted(li, index=0):
    if index == (len(li) - 1):
        return True

    current = li[index] <= li[index + 1]

    remaining = is_Sorted(li, index + 1)

    return current and remaining


print(is_Sorted([11, 44, 66]))


def Contains(li, target, index=0):
    if index == len(li):
        return False

    current = li[index] == target
    remaining = Contains(li, target, index + 1)

    return current or remaining


print(Contains([11, 33, 44, 12, 15], 12))
