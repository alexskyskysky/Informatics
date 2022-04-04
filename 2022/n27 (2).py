# Вариант 5 (2022)
with open("C:\\ЕГЭ\\ЕГЭ-22\\Сброник 12 вариантов\\Вариант 5\\Задание 27\\27_B.txt", "r") as f:
    N = int(f.readline())
    Min = [10001] * N
    Min_d3 = [10001] * N
    result = 10000 * 10000
    for i in range(N):
        x = int(f.readline())
        if x % 3 == 0:
            Min_d3[i] = min(x, Min_d3[i - 1])
            Min[i] = min(x, Min[i - 1])
            if i >= 5 and x * Min[i - 5] < result:
                result = x * Min[i - 5]
        else:
            Min[i] = min(x, Min[i - 1])
            if i >= 5 and x * Min_d3[i - 5] < result:
                result = x * Min_d3[i - 5]
print(result)
