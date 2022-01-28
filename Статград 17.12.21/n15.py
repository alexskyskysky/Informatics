def P(x):
    return 19 < x <= 84


def Q(x):
    return 4 < x <= 51


def A(a, b, x):  # a,b - начало и конец отрезка A, они заранее не известны
    return a < x <= b


min_L = 1000
for a in range(4, 85):
    for b in range(a + 1, 85):
        count_F = 0
        for x in range(100):
            F = not (Q(x)) or P(x) or A(a, b, x)
            if F == 1:
                count_F += 1
        L = b - a
        if count_F == 100 and L < min_L:
            min_L = L
print(min_L)
