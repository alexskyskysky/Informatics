f = open("C:\\ЕГЭ\\ЕГЭ-23\\Сборник 14 вариантов\\Вариант 1\\Задание 17\\17.txt")
N = []
for line in f:
    N.append(int(line))
f.close()

count = 0
max_sum = -10000000
min_n = 100000000
sum4 = 0
count4 = 0
for i in range(len(N)):
    if N[i] < min_n:
        min_n = N[i]
    if N[i] % 4 == 0:
        sum4 += N[i]
        count4 += 1
avg4 = sum4 / count4
for i in range(1, len(N)):
    if (N[i] % min_n == 0 or N[i - 1] % min_n == 0) and (N[i] + N[i - 1] < avg4):
        count += 1
        if N[i] + N[i - 1] > max_sum:
            max_sum = N[i] + N[i - 1]
print(count, max_sum)
