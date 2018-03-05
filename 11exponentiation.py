def exp_recursive(b, n):
    if b == 0:
        return 0

    if n == 1:
        return b
    elif n == 0:
        return 1

    return exp_recursive(b, n - 1) * b


def exp_while(b, n):
    if b == 0:
        return 0

    res = 1

    while n > 0:
        res = res * b
        n -= 1

    return res


print(exp_recursive(5, 3))  # 125
print(exp_recursive(2, 4))  # 16
print(exp_recursive(5, 1))  # 5
print(exp_recursive(6, 0))  # 1

print(exp_while(5, 3))  # 125
print(exp_while(2, 4))  # 16
print(exp_while(5, 1))  # 5
print(exp_while(6, 0))  # 1
