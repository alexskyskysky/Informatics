def F(x):
    N = 243 ** 5 - 3 ** 7 - 2 - x
    count = 0
    while N > 0:
        d = N % 3
        if d == 2:
            count += 1
        N //= 3
    return count


for x in range(1, 1000):
    if F(x) == 20:
        print(x)
        break
