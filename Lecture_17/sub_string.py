def Sub_string(a, b):
    if len(a) == 0 or len(b) == 0:
        return 0

    if a[0] == b[0]:
        return 1 + Sub_string(a[1:], b[1:])
    else:
        left = Sub_string(a[1:], b)
        right = Sub_string(a, b[1:])
        return max(left, right)


print(Sub_string("Naman ", "aman "))


def ret_Sub_string(a, b):
    if len(a) == 0 or len(b) == 0:
        return 0, ""

    if a[0] == b[0]:
        count, max_yet = ret_Sub_string(a[1:], b[1:])
        return count + 1, a[0] + max_yet
    else:
        left, left_yet = ret_Sub_string(a[1:], b)
        right, right_yet = ret_Sub_string(a, b[1:])
        if left > right:
            return left, left_yet
        else:
            return right, right_yet


print(ret_Sub_string("naman", "aman"))


def ret_li_string(a, b):
    if len(a) == 0 or len(b) == 0:
        return 0, [""]

    if a[0] == b[0]:
        count, max_yet = ret_li_string(a[1:], b[1:])
        return count + 1, [a[0]+item for item in max_yet]
    else:
        left, left_yet = ret_li_string(a[1:], b)
        right, right_yet = ret_li_string(a, b[1:])
        if left > right:
            return left, left_yet
        elif left < right:
            return right, right_yet
        else:
            return left, left_yet + right_yet


f, z = ret_li_string("aabbbbaaccaacc", "ccaabbbbaaccccaa")
print(f, set(z))
