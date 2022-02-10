def P(x):
    return 69 < x <= 91


def Q(x):
    return 77 < x <= 114


def A(a, b, x):
    return a < x <= b


min_L = 1000
for a in range(50, 120):
    for b in range(a + 1, 120):
        count_F = 0
        for x in range(150):
            F = (not Q(x)) or ((P(x) == Q(x)) or (P(x) or A(a, b, x)))
            if F == 1:
                count_F += 1
        if count_F == 150 and b - a < min_L:
            min_L = b - a
print(min_L)
