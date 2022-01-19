f = open("C:\\ЕГЭ-22\\Сброник 12 вариантов\\Вариант 1\\Задание 17\\17.txt", "r")
N = []
for line in f:
    N.append(int(line))
f.close()

count = 0
max_sum = -20001
for i in range(1, len(N)):
    if N[i - 1] % 5 == 0 and N[i] % 5 == 0:
        count += 1
        if N[i - 1] + N[i] > max_sum:
            max_sum = N[i - 1] + N[i]
print(count, max_sum)
