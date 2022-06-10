# Вариант 12 (2022)
f = open("C:\\ЕГЭ\\ЕГЭ-22\\Сброник 12 вариантов\\Вариант 12\\Задание 27\\27_B.txt", "r")
N = int(f.readline())
S = 0
Min = [1000000] * 4
for i in range(N):
    a, b = map(int, f.readline().split())
    S += max(a, b)
    if abs(a - b) < Min[abs(a - b) % 4]:
        Min[abs(a - b) % 4] = abs(a - b)
f.close()

if S % 4 != 0:
    S -= Min[S % 4]
print(S)
