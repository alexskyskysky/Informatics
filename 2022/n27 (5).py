# Вариант 1 (2022 - сборник 20 вариантов)
f = open("D:\\ЕГЭ\\ЕГЭ-22\\Сборник 20 вариантов\\27\\27v1234_B.txt", "r")
N = int(f.readline())
S_div = [0] * 123
Num_div = [0] * 123
S = 0
min_S = 10 ** 11
min_count = 10 ** 7
for n in range(N):
    x = int(f.readline())
    S += x
    if S - S_div[S % 123] == min_S:
        if n - Num_div[S % 123] < min_count:
            min_count = n - Num_div[S % 123]
    elif S - S_div[S % 123] < min_S:
        min_S = S - S_div[S % 123]
        min_count = n - Num_div[S % 123]
    S_div[S % 123] = S
    Num_div[S % 123] = n
f.close()
print(min_count)
