f = open("C:\\ЕГЭ\\ЕГЭ-22\\Сброник 12 вариантов\\Вариант 1\\Задание 27\\27_B.txt", "r")
N = int(f.readline())
Max_d = [0] * 4
# список с максимальными числами для разных остатков от деления на 4
for i in range(N):
    x = int(f.readline())
    if x > Max_d[x % 4]:
        Max_d[x % 4] = x
f.close()

S = sum(Max_d)
print(S)
