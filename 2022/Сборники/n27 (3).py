# Вариант 11 (2022)
f = open("C:\\ЕГЭ\\ЕГЭ-22\\Сброник 12 вариантов\\Вариант 11\\Задание 27\\27_B.txt", "r")
N = int(f.readline())
S = 0
min_n5 = 1000000
min_n7 = 1000000
for i in range(N):
    a, b = map(int, f.readline().split())
    S += max(a, b)
    if abs(a - b) % 5 != 0 and abs(a - b) < min_n5:
        min_n5 = abs(a - b)
    if abs(a - b) % 7 != 0 and abs(a - b) < min_n7:
        min_n7 = abs(a - b)
f.close()

if S % 5 == 0 or S % 7 == 0:
    S -= min(min_n7, min_n5)
    if S % 5 == 0 or S % 7 == 0:
        S += min(min_n7, min_n5)
        S -= max(min_n7, min_n5)
        if S % 5 == 0 or S % 7 == 0:
            S += max(min_n7, min_n5)
            S -= min_n5 + min_n7
print(S)
