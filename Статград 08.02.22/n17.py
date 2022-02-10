f = open("D:\\ЕГЭ\\ЕГЭ-22\\Статград 08.02.22\\17.txt", "r")
N = []
for line in f:
    N.append(int(line))
f.close()

count_even = 0  # количество чётных
sum_even = 0  # сумма чётных
for i in range(len(N)):
    if N[i] % 2 == 0:
        count_even += 1
        sum_even += N[i]
avg = sum_even / count_even  # среднее арифметическое чётных
count = 0
max_sum = -1
for i in range(1, len(N)):
    if (N[i - 1] % 3 == 0 and N[i] % 3 != 0 and N[i] < avg) or (N[i] % 3 == 0 and N[i - 1] % 3 != 0 and N[i - 1] < avg):
        count += 1
        if N[i - 1] + N[i] > max_sum:
            max_sum = N[i - 1] + N[i]
print(count, max_sum)
