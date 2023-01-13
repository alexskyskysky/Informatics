def F(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    if n > 2 and n % 3 == 0:
        return 2 * n - F(n // 3) - F(n - 1)
    else:
        return n + F(n - 2) + F(n // 10)


count = 0
for n in range(50, 101):
    if 50 < F(n) <= 200:
        count += 1

print(count)
