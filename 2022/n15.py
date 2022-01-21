# Вариант 1 (2022)
def X(x):
    return 12 < x <= 93


def Y(x):
    return 54 < x <= 150


def Z(a, b, x):
    return a < x <= b


min_L = 100000
for a in range(10, 155):
    for b in range(a + 1, 155):
        count_F = 0
        for x in range(155):
            F = not (Y(x)) or X(x) or Z(a, b, x)
            if F == 1:
                count_F += 1
        if count_F == 155 and b - a < min_L:
            min_L = b - a
print(min_L)
