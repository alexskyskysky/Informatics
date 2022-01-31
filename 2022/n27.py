# Вариант 1 (2022)
d0 = []  # список с числами, у которых остаток от деления на 4 равен 0
d1 = []  # список с числами, у которых остаток от деления на 4 равен 1
d2 = []  # список с числами, у которых остаток от деления на 4 равен 2
d3 = []  # список с числами, у которых остаток от деления на 4 равен 3
with open(
    "C:\\ЕГЭ-22\\Сброник 12 вариантов\\Вариант 1\\Задание 27\\27_B.txt", "r"
) as f:
    N = int(f.readline().strip())
    for i in range(N):
        n = int(f.readline().strip())
        if n % 4 == 0:
            d0.append(n)
        elif n % 4 == 1:
            d1.append(n)
        elif n % 4 == 2:
            d2.append(n)
        else:
            d3.append(n)
S = max(d0) + max(d1) + max(d2) + max(d3)
print(S)
