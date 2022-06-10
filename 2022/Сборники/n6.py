# Вариант 1 (2022)
for n in range(1, 1000):
    x = 0
    p = 0
    a = n
    while p + x < 1050:
        p += a
        x += 1
    if x == 19:
        print(n)
        break
