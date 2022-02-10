def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 3 == 2:
        return F(n - 1) + 1
    if n > 0 and n % 3 < 2:
        return F((n - n % 3) / 3)


for n in range(1000):
    if F(n) == 6:
        print(n)
        break
